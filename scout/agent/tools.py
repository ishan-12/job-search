"""
DB-layer tools for the Scout agent: Python helpers called directly by
runner.py (create_scrape_run, save_jobs, get_existing_job_ids, etc.).
"""

import logging
import sys
import uuid
from datetime import datetime, timezone
from urllib.parse import urlparse, parse_qs, unquote

import duckdb

from app.database import get_connection, find_original_job


def _unwrap_linkedin_redirect(url: str | None) -> str | None:
    """Extract the real destination from a linkedin.com/safety/go redirect URL."""
    if not url:
        return None
    if "linkedin.com/safety/go" in url:
        params = parse_qs(urlparse(url).query)
        if "url" in params:
            return unquote(params["url"][0])
    return url


def create_scrape_run(
    search_name: str,
    linkedin_url: str,
) -> str:
    """Insert a new scrape_run row and return its run_id."""
    run_id = str(uuid.uuid4())
    conn = get_connection()
    conn.execute(
        """
        INSERT INTO scrape_runs (run_id, search_name, linkedin_search_url)
        VALUES (?, ?, ?)
        """,
        [run_id, search_name, linkedin_url],
    )
    conn.close()
    return run_id


def get_existing_job_ids() -> list[str]:
    """Return EVERY job_id already in the DB, dismissed ones included.

    A global, role-agnostic dedup skip-list: a job_id is globally unique and
    its role is derived from its title at save time, so dedup doesn't need a
    run-level role.

    Dismissed jobs must be in this list. They were deliberately excluded here
    once (``WHERE status != 'dismissed'``), on the reasoning that a dismissed
    job is inactive — but the caller uses this as a SKIP-list
    (``apply_deterministic_filters``: ``if job_id in existing_ids: continue``),
    so excluding a job_id means it is *not* skipped. Dismissing a job therefore
    resurrected it: every later run re-cleaned it (Haiku) and re-enriched it
    (Sonnet), then ``save_jobs``' INSERT hit ``job_id VARCHAR PRIMARY KEY`` and
    raised, killing the run. LinkedIn keeps returning the same ids for the whole
    ``f_TPR`` window, so this recurred for as long as the search window is wide.

    Dismissing a job is a decision to stop seeing it. Keeping its id here is what
    makes that decision stick, and costs one row in a set.
    """
    conn = get_connection()
    rows = conn.execute("SELECT job_id FROM jobs").fetchall()
    conn.close()
    return [r[0] for r in rows]


def save_jobs(scrape_run_id: str, jobs: list[dict]) -> dict:
    """
    Persist a list of enriched jobs. Assumes the caller (apply_deterministic_filters,
    via one earlier get_existing_job_ids() fetch) already dropped jobs already in
    the DB, applied, closed, or from an excluded company (config [filters]
    exclude_companies) — nothing between that filter and here changes a job's
    company, so this trusts it rather than re-checking. Detects reposts, and
    persists each job's role_type, description_summary, and tags (produced by
    the per-job enrichment step in runner.py). Returns a summary of what was
    saved.
    """
    saved, reposts, skipped = 0, 0, 0
    conn = get_connection()

    for job in jobs:
        # `or ""` (not a .get default): the scrape can yield company = None.
        company = job.get("company") or ""

        job_id = job["job_id"]

        # Unwrap LinkedIn safety redirects on the apply URL
        job["apply_url"] = _unwrap_linkedin_redirect(job.get("apply_url"))

        # Repost detection
        original_id = find_original_job(conn, job["title"], company)
        is_repost = original_id is not None

        # Per-job try/except, not one transaction for the batch. A run costs a
        # browser scrape plus two LLM calls per job; letting a single bad row
        # (duplicate job_id, malformed field) abort the loop would throw all of
        # that away and — because save_jobs only runs at the very end of a
        # search — lose every other job scraped alongside it. Skip the row, keep
        # the batch.
        try:
            conn.execute(
                """
            INSERT INTO jobs (
                job_id, scrape_run_id, title, company, location, role_type,
                linkedin_url, apply_url, apply_platform, salary_range,
                description_raw, description_clean, description_summary, tags,
                fit_score, criteria_score, dealbreakers, match_reason,
                match_score, status, is_repost, original_job_id, date_scraped
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'new', ?, ?, ?)
            """,
                [
                    job_id,
                    scrape_run_id,
                    job["title"],
                    company,
                    job.get("location"),
                    job.get("role_type"),
                    job.get("linkedin_url"),
                    job.get("apply_url"),
                    job.get("apply_platform", "other"),
                    job.get("salary_range"),
                    job.get("description_raw"),
                    job.get("description_clean"),
                    job.get("description_summary"),
                    job.get("tags") or [],
                    job.get("fit_score"),
                    job.get("criteria_score"),
                    job.get("dealbreakers") or [],
                    job.get("match_reason"),
                    job.get("match_score"),
                    is_repost,
                    original_id,
                    datetime.now(timezone.utc).isoformat(),
                ],
            )
        except duckdb.Error as exc:
            print(f"  save failed for {job_id} ({company}): {exc} — skipping",
                  file=sys.stderr)
            logging.getLogger("scout").warning(
                "save_jobs skipped %s (%s): %s", job_id, company, exc)
            skipped += 1
            continue

        if is_repost:
            reposts += 1
        saved += 1

    # Update jobs_found count on the run
    conn.execute(
        "UPDATE scrape_runs SET jobs_found = jobs_found + ? WHERE run_id = ?",
        [saved, scrape_run_id],
    )
    conn.close()

    return {
        "saved": saved,
        "reposts_detected": reposts,
        "skipped": skipped,
    }
