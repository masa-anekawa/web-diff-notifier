from unittest.mock import MagicMock, patch

import pytest
from bs4 import BeautifulSoup

from src.scraper import Scraper


@pytest.fixture
def scraper():
    urls = ["https://example.com", "https://example.org"]
    return Scraper(urls)


def test_init(scraper):
    assert scraper.urls == ["https://example.com", "https://example.org"]


@patch("requests.get")
def test_scrape(mock_get, scraper):
    mock_response = MagicMock()
    mock_response.text = "<html><body><h1>Example</h1></body></html>"
    mock_get.return_value = mock_response

    scraped_data = scraper.scrape()

    assert len(scraped_data) == 2
    assert all(isinstance(soup, BeautifulSoup) for soup in scraped_data.values())
    mock_get.assert_called()
