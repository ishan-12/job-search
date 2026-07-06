#!/usr/bin/env node
// Resume Markdown -> styled HTML -> PDF (via headless Chrome).
// The .md files are the source of truth; PDFs are generated artifacts.
//
// The output PDF is always named "Resume_Ishan_Shah.pdf" (what recruiters see),
// written next to the source .md. Each resume folder holds one resume, so no collisions.
//
// Usage:
//   node tools/md-to-pdf.mjs <input.md> [output.pdf]   # output defaults to Resume_Ishan_Shah.pdf
//   node tools/md-to-pdf.mjs --all          # regenerate every Resume_*.md in resumes/
//
// No npm dependencies. Renders the small Markdown subset resumes use
// (h1-h3, bold, italic, inline code, links, bullet lists, ---). Blockquotes
// (editorial "> note" lines) are intentionally dropped from the PDF.

import { execFileSync } from "node:child_process";
import { readFileSync, writeFileSync, readdirSync, statSync, mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname, basename, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

export const REPO_ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
export const OUTPUT_NAME = "Resume_Ishan_Shah.pdf"; // recruiter-facing filename for every variant

export const pdfPathFor = (mdPath) => join(dirname(mdPath), OUTPUT_NAME);

export const CHROME = [
  process.env.CHROME_PATH,
  process.env.CHROME_BIN,
  "/usr/bin/chromium",             // Docker (Debian)
  "/usr/bin/chromium-browser",
  "/usr/bin/google-chrome",
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary",
  "/Applications/Chromium.app/Contents/MacOS/Chromium",
  "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
].filter(Boolean).find((p) => { try { statSync(p); return true; } catch { return false; } });

function esc(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

export function inline(s) {
  // order matters: escape first, then apply inline markup
  s = esc(s);
  s = s.replace(/`([^`]+)`/g, "<code>$1</code>");
  s = s.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  s = s.replace(/(^|[^*])\*([^*]+)\*/g, "$1<em>$2</em>");
  s = s.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
  return s;
}

export function mdToHtml(md) {
  const lines = md.split(/\r?\n/);
  const out = [];
  let inList = false;
  const closeList = () => { if (inList) { out.push("</ul>"); inList = false; } };

  for (let raw of lines) {
    const line = raw.replace(/\s+$/, "");
    if (line.startsWith(">")) continue;                 // drop editorial notes
    if (/^---+$/.test(line)) { closeList(); out.push("<hr>"); continue; }
    if (line.trim() === "") { closeList(); continue; }

    let m;
    if ((m = line.match(/^#\s+(.*)/)))   { closeList(); out.push(`<h1>${inline(m[1])}</h1>`); continue; }
    if ((m = line.match(/^##\s+(.*)/)))  { closeList(); out.push(`<h2>${inline(m[1])}</h2>`); continue; }
    if ((m = line.match(/^###\s+(.*)/))) { closeList(); out.push(`<h3>${inline(m[1])}</h3>`); continue; }
    if ((m = line.match(/^[-*]\s+(.*)/))) {
      if (!inList) { out.push("<ul>"); inList = true; }
      out.push(`<li>${inline(m[1])}</li>`);
      continue;
    }
    closeList();
    out.push(`<p>${inline(line)}</p>`);
  }
  closeList();
  return out.join("\n");
}

const CSS = `
  @page { size: Letter; margin: 0.5in 0.6in; }
  * { box-sizing: border-box; }
  body { font-family: "Calibri","Carlito","Helvetica Neue",Arial,sans-serif; color:#1a1a1a;
         font-size: 10.2pt; line-height: 1.32; margin:0; }
  h1 { text-align:center; font-size: 21pt; margin:0 0 2px; letter-spacing:.3px; }
  /* contact line + title line are the two <p> right after h1 */
  h1 + p { text-align:center; margin:0 0 1px; font-size: 9.6pt; color:#333; }
  h1 + p + p { text-align:center; margin:0 0 6px; font-weight:700; font-size:10.6pt; color:#1a3e6f; }
  h2 { font-size: 11pt; text-transform:uppercase; letter-spacing:.6px; color:#1a3e6f;
       border-bottom: 1.2px solid #1a3e6f; padding-bottom:2px; margin: 12px 0 6px; }
  h3 { font-size: 10.4pt; margin: 8px 0 2px; }
  p { margin: 0 0 5px; }
  ul { margin: 2px 0 6px; padding-left: 16px; }
  li { margin: 0 0 2.5px; }
  hr { border:0; border-top:0; height:0; margin:4px 0; }
  hr:first-of-type { display:none; }
  a { color:#1a3e6f; text-decoration:none; }
  code { font-family: "SF Mono",Menlo,monospace; font-size:9pt; background:#f2f2f2; padding:0 3px; border-radius:3px; }
  strong { font-weight:700; }
  h3 + ul { margin-top:2px; }
`;

export function buildOne(mdPath, pdfPath) {
  if (!CHROME) {
    throw new Error(
      "No Chrome/Chromium/Edge found for PDF rendering. In Docker set CHROME_PATH=/usr/bin/chromium."
    );
  }
  const md = readFileSync(mdPath, "utf8");
  const html = `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>${mdToHtml(md)}</body></html>`;
  const tmp = mkdtempSync(join(tmpdir(), "resume-"));
  const htmlPath = join(tmp, "resume.html");
  writeFileSync(htmlPath, html);
  try {
    execFileSync(CHROME, [
      "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
      "--no-sandbox", "--disable-dev-shm-usage", // required when running as root in Docker
      // keep all Chromium scratch under our temp dir so it works with a read-only root fs
      `--user-data-dir=${join(tmp, "chrome")}`, `--crash-dumps-dir=${join(tmp, "crash")}`,
      `--print-to-pdf=${pdfPath}`, `file://${htmlPath}`,
      // hard timeout so a stuck render fails loudly instead of hanging forever
    ], { stdio: "ignore", timeout: 120000, killSignal: "SIGKILL" });
    console.log(`  ✓ ${basename(pdfPath)}`);
  } finally {
    rmSync(tmp, { recursive: true, force: true });
  }
}

export function findResumes(dir, acc = []) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    const st = statSync(p);
    if (st.isDirectory()) { if (name !== "_TEMPLATE") findResumes(p, acc); }
    else if (/^Resume_.*\.md$/.test(name)) acc.push(p);
  }
  return acc;
}

function main() {
  const args = process.argv.slice(2);
  if (args[0] === "--all") {
    const files = findResumes(join(REPO_ROOT, "resumes"));
    console.log(`Generating ${files.length} resume PDF(s):`);
    for (const f of files) buildOne(f, pdfPathFor(f));
  } else if (args[0]) {
    const mdPath = resolve(args[0]);
    buildOne(mdPath, args[1] ? resolve(args[1]) : pdfPathFor(mdPath));
  } else {
    console.error("Usage: node tools/md-to-pdf.mjs <input.md> [output.pdf] | --all");
    process.exit(1);
  }
}

// Run the CLI only when executed directly, not when imported by tests.
if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  main();
}
