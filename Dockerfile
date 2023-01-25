FROM registry.gitlab.com/cloudybay/{{ repository_name }}:base

ARG PROJECT_DIR=/app

COPY --chown=cloudybay . $PROJECT_DIR

WORKDIR $PROJECT_DIR

RUN python3 init_env.py && DJANGO_SETTINGS_MODULE=wd.settings python3 manage.py collectstatic --no-input
