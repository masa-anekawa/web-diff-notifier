import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, urls):
        self.urls = urls

    def scrape(self):
        scraped_data = {}
        for url in self.urls:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "lxml")
            scraped_data[url] = soup
        return scraped_data
