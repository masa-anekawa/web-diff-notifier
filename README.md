# Web Scraping and Diff Detection App

This Python application performs web scraping, HTML diff detection, and sends notifications when specific changes are detected on a webpage.

## Features

- Web Scraping: Periodically access predefined URLs and parse the content using BeautifulSoup4.
- HTML Diff Detection: Analyze the parsed content and detect differences in DOM tree elements based on predefined XPaths.
- Diff Notification: Send a POST HTTP request with the detected diff text to a predefined URL when the diff contains specific strings.

## Prerequisites

- Python 3.12
- Docker

## Setup

1. Install Poetry:

  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  ```

2. Install dependencies:

  ```bash
  poetry install
  ```

## Configuration

Edit the `src/config.py` file to configure the following:
- `SCRAPING_URLS`: List of URLs to scrape.
- `DIFF_XPATHS`: XPaths to detect differences in the DOM tree.
- `NOTIFICATION_URL`: URL to send the POST request with the detected diff.
- `NOTIFICATION_STRINGS`: List of strings to trigger a notification when found in the diff.

## Usage

Run the application using Docker:

```bash
docker build -t web-scraper-diff-detector .
docker run web-scraper-diff-detector
```

## Development

- The application uses Poetry and Pyenv for environment management.
- All code follows Python best practices and is highly refined.
- The `src` directory contains the main application code.

## License

This project is licensed under the MIT License.
