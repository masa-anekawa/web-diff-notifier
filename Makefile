.PHONY: install build clean

install:
	poetry install

build:
	docker build -t web-scraper-diff-detector .

clean:
	docker rmi web-scraper-diff-detector
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -exec rm -f {} +
	find . -type f -name "*.pyo" -exec rm -f {} +
	find . -type f -name "*.pyd" -exec rm -f {} +
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .hypothesis
