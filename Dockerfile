FROM python:3.10-slim-buster AS builder

RUN apt-get update && apt-get install -y git

RUN python3 -m venv /opt/venv

COPY requirements.txt /

RUN /opt/venv/bin/python3 -m pip install -r /requirements.txt && /opt/venv/bin/python3 -m pip cache purge

#######################################################

FROM python:3.10-slim-buster AS base

COPY --from=builder /opt/venv /opt/venv

ENV PATH=/opt/venv/bin:$PATH

WORKDIR $PROJECT_DIR

#######################################################

FROM base AS source

ARG PROJECT_DIR=/app
ARG PROJECT_LOG_DIR=/var/log/app
RUN mkdir -p $PROJECT_LOG_DIR \
    && mkdir -p $PROJECT_DIR

RUN groupadd -r cloudybay -g 1000 && useradd -m -g 1000 cloudybay -u 1000
RUN chown -R cloudybay:1000 $PROJECT_DIR \
    && chown -R cloudybay:1000 $PROJECT_LOG_DIR \
    && chown -R cloudybay:1000 /opt/venv

COPY --chown=cloudybay:1000 . $PROJECT_DIR

USER cloudybay

WORKDIR $PROJECT_DIR
ENV DJANGO_SETTINGS_MODULE=tcf.settings
ENV PYTHONPATH=$PROJECT_DIR
ENV BASE_DIR=$PROJECT_DIR