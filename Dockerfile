FROM python:3.10-slim-buster AS builder

RUN apt-get update && apt-get install -y git

RUN groupadd -r cloudybay -g 1000 && useradd -m -g 1000 cloudybay -u 1000
USER cloudybay

COPY requirements.txt /

RUN pip3 install -r /requirements.txt && pip cache purge

#######################################################

FROM python:3.10-slim-buster AS base

ARG PROJECT_DIR=/app
ARG PROJECT_LOG_DIR=/var/log/app
RUN mkdir -p $PROJECT_LOG_DIR \
    && mkdir -p $PROJECT_DIR

RUN groupadd -r cloudybay -g 1000 && useradd -m -g 1000 cloudybay -u 1000
RUN chown -R cloudybay:1000 $PROJECT_DIR \
    && chown -R cloudybay:1000 $PROJECT_LOG_DIR

ENV PATH=$PATH:/home/cloudybay/.local/bin

COPY --from=builder /home/cloudybay /home/cloudybay

USER cloudybay

WORKDIR $PROJECT_DIR

#######################################################

FROM base AS source

ARG PROJECT_DIR=/app

COPY --chown=cloudybay:1000 . $PROJECT_DIR

WORKDIR $PROJECT_DIR

ENV PYTHONPATH=/app
