#!/bin/bash
set -e

rsync -avh \
    --exclude=.git \
    /tmp/project/ $IMAGE_PROJECT_DIR

WORK_DIR=$IMAGE_PROJECT_DIR
PYTHON=/usr/bin/python3.6

$PYTHON manage.py migrate
$PYTHON manage.py collectstatic --no-input
$PYTHON bin/rp_filedrived.py -d
$PYTHON bin/rp_timedrived.py -d

/usr/local/bin/gunicorn \
    --preload \
    --bind 0.0.0.0:8080 {PROJECT_NAME}.wsgi \
    --error-logfile $WORK_DIR/logfiles/gunicorn.error.log \
    --access-logfile $WORK_DIR/logfiles/gunicorn.access.log \
    --timeout 360 --workers 3 --max-requests 10000

exec "$@"
