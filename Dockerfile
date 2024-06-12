FROM python:3.12-slim-bookworm

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY src ./src

CMD ["python", "src/main.py"]
