# syntax=docker/dockerfile:1
FROM python:3.10

RUN addgroup --system vulpecula
RUN adduser --system vulpecula --ingroup vulpecula
USER vulpecula:vulpecula

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="/home/vulpecula/.poetry/bin:$PATH"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY ./pyproject.toml ./pyproject.toml 
RUN poetry install
