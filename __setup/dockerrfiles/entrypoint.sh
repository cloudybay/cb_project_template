#!/bin/bash
set -e

WORK_DIR=$IMAGE_PROJECT_DIR
PYTHON=/usr/bin/python3.6
GOSU=/usr/local/bin/gosu
USER_NAME=$1
USER_ID=$2

rsync -avh \
    --exclude=.git \
    /tmp/project/ $IMAGE_PROJECT_DIR

groupadd -r $USER_NAME -g $USER_ID && useradd -m -g $USER_NAME $USER_NAME -u $USER_ID

chown -R $USER_ID:$USER_ID /opt/CloudyBay

$GOSU $USER_ID $PYTHON manage.py migrate
$GOSU $USER_ID $PYTHON manage.py collectstatic --no-input
$GOSU $USER_ID $PYTHON bin/{{ project_name }}_filedrived.py -d
$GOSU $USER_ID $PYTHON bin/{{ project_name }}_timedrived.py -d

$GOSU $USER_ID /usr/local/bin/gunicorn \
    --preload \
    --bind 0.0.0.0:8080 {{ project_name }}.wsgi \
    --error-logfile $WORK_DIR/logfiles/gunicorn.error.log \
    --access-logfile $WORK_DIR/logfiles/gunicorn.access.log \
    --timeout 360 --workers 3 --max-requests 10000
