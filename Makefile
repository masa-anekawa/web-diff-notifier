.PHONY: install build clean test coverage lint format

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

test:
	poetry run pytest tests/unit

coverage:
	poetry run pytest --cov=src --cov-report=term-missing tests/unit

lint:
	poetry run pylint src tests
	poetry run flake8 src tests

format:
	poetry run black src tests
	poetry run isort src tests

ci: format lint test coverage
