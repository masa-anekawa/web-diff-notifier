import pytest
from unittest.mock import MagicMock
from src.diff_detector import DiffDetector


@pytest.fixture
def diff_detector():
    xpaths = ["/html/body/h1", "/html/body/p"]
    return DiffDetector(xpaths)


def test_init(diff_detector):
    assert diff_detector.xpaths == ["/html/body/h1", "/html/body/p"]
    assert diff_detector.previous_data == {}


def test_detect_diffs(diff_detector):
    scraped_data = {
        "https://example.com": MagicMock(),
        "https://example.org": MagicMock(),
    }
    scraped_data["https://example.com"].select.return_value = ["<h1>Example</h1>"]
    scraped_data["https://example.org"].select.return_value = ["<p>Example</p>"]

    diffs = diff_detector.detect_diffs(scraped_data)

    assert len(diffs) == 2
    assert all(isinstance(diff, dict) for diff in diffs.values())
    scraped_data["https://example.com"].select.assert_called()
    scraped_data["https://example.org"].select.assert_called()
