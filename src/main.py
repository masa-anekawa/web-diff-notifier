from scraper import Scraper
from diff_detector import DiffDetector
from notifier import Notifier
from config import SCRAPING_URLS, DIFF_XPATHS, NOTIFICATION_URL, NOTIFICATION_STRINGS


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
