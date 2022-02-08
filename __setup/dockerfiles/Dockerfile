FROM registry.gitlab.com/cloudybay/{{ repository_name }}:base

ARG TMP_PROJECT_DIR=/tmp/project

COPY . $TMP_PROJECT_DIR

RUN mkdir $TMP_PROJECT_DIR/logfiles || true

ARG IMAGE_PROJECT_DIR
RUN mkdir -p $IMAGE_PROJECT_DIR

WORKDIR $IMAGE_PROJECT_DIR
