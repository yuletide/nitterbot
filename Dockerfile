# https://stackoverflow.com/questions/72465421/how-to-use-poetry-with-docker
FROM python:3.9-slim as base
# python:3.10-slim-bullseye
# https://pythonspeed.com/articles/base-image-python-docker-images/

# ARG YOUR_ENV

# Configure Poetry
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random

WORKDIR /app

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.3.1
# YOUR_ENV=${YOUR_ENV} \

ENV PATH="/root/.local/bin:$PATH"

# RUN python -m pip install -U pip "poetry==$POETRY_VERSION"
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml /app/

# Project initialization:
# poetry install $(test "$YOUR_ENV" == production && echo "--no-dev")
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-root --no-dev && \
    rm -rf ~/.cache/pypoetry && \
    rm -rf ~/.config/pypoetry

# ADD main.py .
COPY . /app

CMD ["python", "-m", "nitterbot"]
