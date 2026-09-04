import io
import json
import urllib.error
import unittest
from unittest import mock

from tools.catalog import github_repo_state


class _Response:
    def __init__(self, payload):
        self._payload = json.dumps(payload).encode("utf-8")

    def __enter__(self):
        return io.BytesIO(self._payload)

    def __exit__(self, exc_type, exc, tb):
        return False


class CatalogNetworkTests(unittest.TestCase):
    def test_404_is_missing_without_retry(self):
        error = urllib.error.HTTPError(
            "https://api.github.com/repos/owner/missing",
            404,
            "Not Found",
            {},
            None,
        )
        with mock.patch("tools.catalog.urllib.request.urlopen", side_effect=error) as urlopen, mock.patch(
            "tools.catalog.time.sleep"
        ) as sleep:
            self.assertEqual(github_repo_state("owner/missing", None), {"status": "MISSING"})
        self.assertEqual(urlopen.call_count, 1)
        sleep.assert_not_called()

    def test_transient_http_failure_retries_then_succeeds(self):
        error = urllib.error.HTTPError(
            "https://api.github.com/repos/owner/repo",
            503,
            "Service Unavailable",
            {},
            None,
        )
        payload = {
            "archived": False,
            "private": False,
            "full_name": "owner/repo",
            "default_branch": "main",
            "html_url": "https://github.com/owner/repo",
        }
        with mock.patch(
            "tools.catalog.urllib.request.urlopen",
            side_effect=[error, _Response(payload)],
        ) as urlopen, mock.patch("tools.catalog.time.sleep") as sleep:
            state = github_repo_state("owner/repo", None)
        self.assertEqual(state["status"], "ACTIVE")
        self.assertEqual(urlopen.call_count, 2)
        sleep.assert_called_once_with(1.0)

    def test_rate_limit_honors_retry_after(self):
        error = urllib.error.HTTPError(
            "https://api.github.com/repos/owner/repo",
            429,
            "Too Many Requests",
            {"Retry-After": "7"},
            None,
        )
        payload = {
            "archived": True,
            "private": False,
            "full_name": "owner/repo",
            "default_branch": "main",
            "html_url": "https://github.com/owner/repo",
        }
        with mock.patch(
            "tools.catalog.urllib.request.urlopen",
            side_effect=[error, _Response(payload)],
        ), mock.patch("tools.catalog.time.sleep") as sleep:
            state = github_repo_state("owner/repo", "token")
        self.assertEqual(state["status"], "ARCHIVED")
        sleep.assert_called_once_with(7.0)

    def test_network_failure_uses_bounded_retries_then_reraises(self):
        error = urllib.error.URLError("temporary DNS failure")
        with mock.patch(
            "tools.catalog.urllib.request.urlopen",
            side_effect=error,
        ) as urlopen, mock.patch("tools.catalog.time.sleep") as sleep:
            with self.assertRaises(urllib.error.URLError):
                github_repo_state("owner/repo", None)
        self.assertEqual(urlopen.call_count, 3)
        self.assertEqual([call.args[0] for call in sleep.call_args_list], [1.0, 2.0])


if __name__ == "__main__":
    unittest.main()
