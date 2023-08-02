#!/bin/bash
set -e

gunicorn \
    --preload \
    --bind 0.0.0.0:8000 {{ project_name }}.wsgi \
    --timeout 360 --workers 5 --max-requests 10000 \
    --pid /var/run/app/gunicorn.pid
