FROM python:3.10-slim

# avoid block buffering
ENV PYTHONUNBUFFERED=1

ENV PATH=/etc/poetry/bin:$PATH
ENV POETRY_VIRTUALENVS_CREATE=0
ENV POETRY_HOME=/etc/poetry/

ADD https://raw.githubusercontent.com/python-poetry/install.python-poetry.org/main/install-poetry.py /tmp/install-poetry.py
RUN python /tmp/install-poetry.py

# create non-root user
RUN groupadd -g 999 localuser && \
    useradd -r -u 999 -g localuser localuser

WORKDIR /app
ADD . /app/
RUN poetry install --no-dev --no-root

USER localuser

EXPOSE 8000