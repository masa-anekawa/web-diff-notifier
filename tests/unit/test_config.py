from src.config import DIFF_XPATHS, NOTIFICATION_STRINGS, NOTIFICATION_URL, SCRAPING_URLS


def test_scraping_urls():
    assert isinstance(SCRAPING_URLS, list)
    assert all(isinstance(url, str) for url in SCRAPING_URLS)


def test_diff_xpaths():
    assert isinstance(DIFF_XPATHS, list)
    assert all(isinstance(xpath, str) for xpath in DIFF_XPATHS)


def test_notification_url():
    assert isinstance(NOTIFICATION_URL, str)


def test_notification_strings():
    assert isinstance(NOTIFICATION_STRINGS, list)
    assert all(isinstance(string, str) for string in NOTIFICATION_STRINGS)
