FROM python:3.10

# avoid block buffering
ENV PYTHONUNBUFFERED=1

# create non-root user
RUN groupadd -g 999 localuser && \
    useradd -r -u 999 -g localuser localuser

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install

USER localuser

EXPOSE 8000