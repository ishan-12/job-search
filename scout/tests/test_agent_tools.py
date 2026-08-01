"""Tests for agent/tools.py — database operations."""

import pytest
from unittest.mock import Mock, patch, MagicMock

from agent.tools import (
    _unwrap_linkedin_redirect,
    create_scrape_run,
    get_existing_job_ids,
    save_jobs,
)


class TestUnwrapLinkedinRedirect:
    """Test LinkedIn safety/go redirect URL unwrapping."""

    def test_unwrap_redirect_url(self):
        """Extract real URL from LinkedIn safety redirect."""
        redirect = "https://www.linkedin.com/safety/go?url=https%3A%2F%2Fexample.com%2Fjob"
        assert _unwrap_linkedin_redirect(redirect) == "https://example.com/job"

    def test_pass_through_regular_url(self):
        """Return non-redirect URLs unchanged."""
        url = "https://example.com/job"
        assert _unwrap_linkedin_redirect(url) == url

    def test_none_input(self):
        """Return None for None input."""
        assert _unwrap_linkedin_redirect(None) is None

    def test_empty_string(self):
        """Return None for empty input."""
        assert _unwrap_linkedin_redirect("") is None

    def test_redirect_without_url_param(self):
        """Return redirect URL unchanged if no url param."""
        redirect = "https://www.linkedin.com/safety/go?other=param"
        assert _unwrap_linkedin_redirect(redirect) == redirect


class TestCreateScrapeRun:
    """Test scrape run creation in database."""

    @patch('agent.tools.get_connection')
    def test_create_scrape_run(self, mock_get_conn):
        """Create a new scrape run and return its ID."""
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn

        run_id = create_scrape_run(
            search_name="Senior IC Bay Area",
            linkedin_url="https://linkedin.com/jobs",
        )

        assert run_id is not None
        assert len(run_id) == 36  # UUID length
        mock_conn.execute.assert_called_once()
        mock_conn.close.assert_called_once()


class TestGetExistingJobIds:
    """Test retrieving existing job IDs from database."""

    @patch('agent.tools.get_connection')
    def test_get_all_job_ids(self, mock_get_conn):
        """Get all non-dismissed job IDs."""
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchall.return_value = [
            ("job1",),
            ("job2",),
            ("job3",),
        ]
        mock_get_conn.return_value = mock_conn

        job_ids = get_existing_job_ids()

        assert job_ids == ["job1", "job2", "job3"]
        mock_conn.execute.assert_called_once()
        # The skip-list must NOT filter on status. This assertion used to read
        # `assert "dismissed" in ...`, which pinned the opposite behaviour and so
        # protected the bug it should have caught — see the regression test in
        # TestDismissedJobsStayDeduped for what that cost.
        assert "dismissed" not in mock_conn.execute.call_args[0][0]

    @patch('agent.tools.get_connection')
    def test_get_empty_job_ids(self, mock_get_conn):
        """Return empty list when no jobs found."""
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchall.return_value = []
        mock_get_conn.return_value = mock_conn

        job_ids = get_existing_job_ids()

        assert job_ids == []


class TestSaveJobs:
    """Test saving enriched jobs to database."""

    @patch('agent.tools.find_original_job')
    @patch('agent.tools.get_connection')
    def test_save_single_job(self, mock_get_conn, mock_find_orig):
        """Save a single job to database."""
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_find_orig.return_value = None

        job = {
            "job_id": "12345",
            "title": "Senior Engineer",
            "company": "TechCorp",
            "location": "Springfield, USA",
            "linkedin_url": "https://linkedin.com/jobs/view/12345",
            "apply_url": "https://example.com/apply",
            "apply_platform": "easy_apply",
            "salary_range": "$150k-$200k",
            "description_raw": "Job description here",
            "description_summary": "Summary",
            "role_type": "IC",
        }

        result = save_jobs("run_id", [job])

        assert result["saved"] == 1
        assert result["reposts_detected"] == 0

    @patch('agent.tools.find_original_job')
    @patch('agent.tools.get_connection')
    def test_save_job_with_null_company(self, mock_get_conn, mock_find_orig):
        """A job whose scrape yielded company = None saves instead of crashing.

        Regression: job.get("company", "") returns None when the key is
        present with a null value, and None.lower() blew up the whole run.
        """
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_find_orig.return_value = None

        job = {
            "job_id": "12345",
            "title": "Engineer",
            "company": None,
            "location": "NYC",
            "linkedin_url": "https://linkedin.com/jobs/view/12345",
            "apply_platform": "easy_apply",
            "description_raw": "Job",
            "role_type": "IC",
        }

        result = save_jobs("run_id", [job])

        assert result["saved"] == 1

    @patch('agent.tools.find_original_job')
    @patch('agent.tools.get_connection')
    def test_detect_repost(self, mock_get_conn, mock_find_orig):
        """Detect and mark reposts."""
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_find_orig.return_value = "original_job_id"

        job = {
            "job_id": "12345",
            "title": "Engineer",
            "company": "TechCorp",
            "location": "NYC",
            "linkedin_url": "https://linkedin.com/jobs/view/12345",
            "apply_platform": "easy_apply",
            "description_raw": "Job",
            "role_type": "IC",
        }

        result = save_jobs("run_id", [job])

        assert result["saved"] == 1
        assert result["reposts_detected"] == 1

    @patch('agent.tools.find_original_job')
    @patch('agent.tools.get_connection')
    def test_unwrap_apply_url(self, mock_get_conn, mock_find_orig):
        """Unwrap LinkedIn safety redirect in apply URLs."""
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_find_orig.return_value = None

        job = {
            "job_id": "12345",
            "title": "Engineer",
            "company": "TechCorp",
            "location": "NYC",
            "linkedin_url": "https://linkedin.com/jobs/view/12345",
            "apply_url": "https://www.linkedin.com/safety/go?url=https%3A%2F%2Fexample.com",
            "apply_platform": "easy_apply",
            "description_raw": "Job",
            "role_type": "IC",
        }

        result = save_jobs("run_id", [job])

        assert result["saved"] == 1
        # Verify the execute was called and the URL was unwrapped
        call_args = mock_conn.execute.call_args_list
        assert any("example.com" in str(call) for call in call_args)


class TestDismissedJobsStayDeduped:
    """A dismissed job must never be re-processed on a later run.

    Regression test for the dedup inversion: get_existing_job_ids() filtered out
    dismissed rows, but its only caller treats the result as a SKIP-list, so a
    dismissed job was excluded from the skip-list and therefore re-scraped,
    re-cleaned (Haiku) and re-enriched (Sonnet) on every subsequent run — then
    crashed the run on save_jobs' INSERT against the job_id PRIMARY KEY.

    These exercise a real DuckDB file rather than mocks, because the bug lived in
    the interaction between the query, the skip-list semantics, and the primary
    key — all three of which mocks would paper over.
    """

    def _seed(self, tmp_path, monkeypatch, status):
        """Create a one-row jobs DB at the given status and point the app at it."""
        import app.database as database
        import agent.tools as tools_mod
        monkeypatch.setattr(database, "DB_PATH", tmp_path / "scout.duckdb")
        database.init_db()
        conn = database.get_connection()
        conn.execute("INSERT INTO scrape_runs (run_id) VALUES ('run1')")
        conn.execute(
            "INSERT INTO jobs (job_id, scrape_run_id, title, company, status) "
            "VALUES ('job-dismissed', 'run1', 'Director of Engineering', 'Acme', ?)",
            [status],
        )
        conn.close()
        return tools_mod

    @pytest.mark.parametrize("status", ["new", "saved", "applied", "dismissed"])
    def test_every_status_is_in_the_skip_list(self, tmp_path, monkeypatch, status):
        """Existing job_ids are returned regardless of status, dismissed included."""
        tools_mod = self._seed(tmp_path, monkeypatch, status)
        assert tools_mod.get_existing_job_ids() == ["job-dismissed"]

    def test_dismissed_job_is_filtered_out_of_a_later_scrape(self, tmp_path, monkeypatch):
        """apply_deterministic_filters drops a previously dismissed job."""
        self._seed(tmp_path, monkeypatch, "dismissed")
        from agent.runner import apply_deterministic_filters
        from agent.tools import get_existing_job_ids

        scraped = {"job-dismissed": {"company": "Acme", "title": "Director of Engineering",
                                     "jobState": "LISTED", "description_raw": "x"}}
        survivors = apply_deterministic_filters(scraped, set(get_existing_job_ids()))
        assert survivors == [], "dismissed job must not be re-processed"

    def test_save_jobs_survives_a_duplicate_row(self, tmp_path, monkeypatch):
        """A duplicate job_id is skipped, and the rest of the batch still saves.

        Before save_jobs hardened its per-job INSERT, one duplicate raised out of
        the loop and lost every other job scraped in the same run.
        """
        tools_mod = self._seed(tmp_path, monkeypatch, "dismissed")
        result = tools_mod.save_jobs("run1", [
            {"job_id": "job-dismissed", "title": "Director of Engineering", "company": "Acme"},
            {"job_id": "job-new", "title": "VP Engineering", "company": "Globex"},
        ])
        assert result["skipped"] == 1
        assert result["saved"] == 1
        assert "job-new" in tools_mod.get_existing_job_ids()
