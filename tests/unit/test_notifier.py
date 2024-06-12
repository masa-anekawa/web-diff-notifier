from unittest.mock import MagicMock, patch
from src.notifier import Notifier


def test_init():
    url = "https://api.example.com/notify"
    trigger_strings = ["important", "urgent"]
    notifier = Notifier(url, trigger_strings)

    assert notifier.url == url
    assert notifier.trigger_strings == trigger_strings


@patch("requests.post")
def test_notify(mock_post):
    notifier = Notifier("https://api.example.com/notify",
                        ["important", "urgent"])
    diffs = {
        "https://example.com": {
            "/html/body/h1": "New important content",
        },
        "https://example.org": {
            "/html/body/p": "New urgent content",
        },
    }

    notifier.notify(diffs)

    assert mock_post.call_count == 2
    mock_post.assert_called_with(
        "https://api.example.com/notify",
        json={
            "url": "https://example.org",
            "xpath": "/html/body/p",
            "diff": "New urgent content",
        },
    )
