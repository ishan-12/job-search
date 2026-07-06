// Tests for the resume PDF generator.
//   node --test tools/         (run locally)
//   docker compose run --rm test   (run in the production image)
//
// Two layers:
//   1. Unit tests for the Markdown -> HTML conversion (pure, no browser).
//   2. "PDF generation never fails" — actually renders every real resume plus a
//      battery of hostile/edge-case inputs and asserts each yields a valid PDF.
import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync, writeFileSync, mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import {
  mdToHtml, inline, buildOne, findResumes, REPO_ROOT, CHROME,
} from "./md-to-pdf.mjs";

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------
function assertValidPdf(pdfPath) {
  const buf = readFileSync(pdfPath);
  // A valid blank page is ~800 bytes; real resumes are ~180 KB. This floor
  // catches truncated/empty output while allowing degenerate-input blank pages.
  assert.ok(buf.length > 400, `PDF suspiciously small: ${buf.length} bytes`);
  assert.equal(buf.subarray(0, 5).toString("latin1"), "%PDF-", "missing %PDF- header");
  assert.ok(
    buf.subarray(-2048).toString("latin1").includes("%%EOF"),
    "missing %%EOF trailer (truncated/corrupt PDF)",
  );
  const pages = (buf.toString("latin1").match(/\/Type\s*\/Page[^s]/g) || []).length;
  assert.ok(pages >= 1, `expected at least 1 page, found ${pages}`);
}

// Render markdown to a PDF in a throwaway temp dir and validate it. Throws on any failure.
function generateAndValidate(md, filename = "Resume_Test.md") {
  const dir = mkdtempSync(join(tmpdir(), "resume-test-"));
  try {
    const mdPath = join(dir, filename);
    writeFileSync(mdPath, md);
    const outPath = join(dir, "out.pdf");
    buildOne(mdPath, outPath);
    assertValidPdf(outPath);
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
}

// ---------------------------------------------------------------------------
// 1. Unit tests — Markdown -> HTML (no browser needed)
// ---------------------------------------------------------------------------
test("mdToHtml: headings map to h1/h2/h3", () => {
  assert.match(mdToHtml("# Title"), /<h1>Title<\/h1>/);
  assert.match(mdToHtml("## Section"), /<h2>Section<\/h2>/);
  assert.match(mdToHtml("### Sub"), /<h3>Sub<\/h3>/);
});

test("mdToHtml: inline bold, italic, code, links", () => {
  assert.match(inline("**b**"), /<strong>b<\/strong>/);
  assert.match(inline("*i*"), /<em>i<\/em>/);
  assert.match(inline("`c`"), /<code>c<\/code>/);
  assert.match(inline("[t](https://x.io)"), /<a href="https:\/\/x\.io">t<\/a>/);
});

test("mdToHtml: consecutive bullets group into a single <ul>", () => {
  const html = mdToHtml("- one\n- two\n- three");
  assert.equal((html.match(/<ul>/g) || []).length, 1);
  assert.equal((html.match(/<li>/g) || []).length, 3);
});

test("mdToHtml: blockquote editorial notes are dropped", () => {
  const html = mdToHtml("> do not tailor this file\n# Real Title");
  assert.doesNotMatch(html, /do not tailor/);
  assert.match(html, /<h1>Real Title<\/h1>/);
});

test("mdToHtml: --- becomes an <hr>", () => {
  assert.match(mdToHtml("a\n\n---\n\nb"), /<hr>/);
});

test("inline: escapes HTML special characters", () => {
  const out = inline("a < b & c > d");
  assert.match(out, /a &lt; b &amp; c &gt; d/);
});

test("inline: neutralizes injected markup (no raw <script>)", () => {
  const out = inline("<script>alert('x')</script>");
  assert.doesNotMatch(out, /<script>/);
  assert.match(out, /&lt;script&gt;/);
});

// ---------------------------------------------------------------------------
// 2. PDF generation never fails — real resumes + hostile edge cases
// ---------------------------------------------------------------------------
const EDGE_CASES = {
  "empty file": "",
  "only whitespace": "   \n\n\t\n   ",
  "only blockquotes (everything dropped)": "> note one\n> note two\n",
  "unicode and emoji": "# Åsa Ødegård 日本語 🚀\n\n- café — naïve — 你好 ✅\n",
  "html special chars": "# a < b & c > d\n\n- 1 < 2 && 3 > 2\n",
  "injected markup is escaped": "# <script>alert('x')</script>\n\n- <img src=x onerror=alert(1)>\n",
  "very long single line": "# T\n\n" + "word ".repeat(1000),
  "many list items": "# List\n\n" + Array.from({ length: 500 }, (_, i) => `- item ${i}`).join("\n"),
  "unbalanced markdown syntax": "# Title **bold and `code never closed\n\n- **\n- `\n",
  "headings only": "# H1\n## H2\n### H3\n",
  "no trailing newline": "# No newline at end of file",
  "windows CRLF line endings": "# Title\r\n\r\n- bullet one\r\n- bullet two\r\n",
};

test("PDF generation: every real resume renders to a valid PDF", { skip: CHROME ? false : "no browser available" }, () => {
  const resumes = findResumes(join(REPO_ROOT, "resumes"));
  assert.ok(resumes.length >= 1, "expected at least one Resume_*.md to exist");
  for (const md of resumes) {
    generateAndValidate(readFileSync(md, "utf8"), "Resume_Real.md");
  }
});

for (const [name, md] of Object.entries(EDGE_CASES)) {
  test(`PDF generation never fails: ${name}`, { skip: CHROME ? false : "no browser available" }, () => {
    generateAndValidate(md);
  });
}
