FROM python:3.12.3-slim-bookworm AS builder

RUN apt-get update && apt-get install -y git libpq-dev && apt clean

RUN python3 -m venv /opt/venv

COPY requirements.txt /

RUN /opt/venv/bin/python3 -m pip install --upgrade pip
RUN /opt/venv/bin/python3 -m pip install -r /requirements.txt && /opt/venv/bin/python3 -m pip cache purge

#######################################################

FROM python:3.12.3-slim-bookworm AS base

RUN apt-get update && apt-get install -y git libpq-dev && apt clean

COPY --from=builder /opt/venv /opt/venv

ENV PATH=/opt/venv/bin:$PATH

#######################################################

FROM base AS source

USER 1000:1000

COPY --chown=1000:1000 . /app

WORKDIR /app
