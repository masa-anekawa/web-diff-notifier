from src.config import DIFF_XPATHS, NOTIFICATION_STRINGS, NOTIFICATION_URL, SCRAPING_URLS
from src.diff_detector import DiffDetector
from src.notifier import Notifier
from src.scraper import Scraper


def main():
    scraper = Scraper(SCRAPING_URLS)
    diff_detector = DiffDetector(DIFF_XPATHS)
    notifier = Notifier(NOTIFICATION_URL, NOTIFICATION_STRINGS)

    while True:
        scraped_data = scraper.scrape()
        diffs = diff_detector.detect_diffs(scraped_data)
        notifier.notify(diffs)


if __name__ == "__main__":
    main()
