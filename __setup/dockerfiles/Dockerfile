FROM registry.gitlab.com/cloudybay/{PROJECT_NAME}:base

ARG TMP_PROJECT_DIR=/tmp/project

COPY . $TMP_PROJECT_DIR

RUN mkdir $TMP_PROJECT_DIR/logfiles || true

RUN cp -f $TMP_PROJECT_DIR/env.py.readme $TMP_PROJECT_DIR/env.py

ARG IMAGE_PROJECT_DIR
RUN mkdir -p $IMAGE_PROJECT_DIR

WORKDIR $IMAGE_PROJECT_DIR

ENTRYPOINT ["/tmp/project/entrypoint.sh"]