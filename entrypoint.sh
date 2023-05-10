#!/bin/bash
set -e

# python3 bin/{{ project_name }}_timedrived.py -d
# python3 bin/{{ project_name }}_filedrived.py -d

gunicorn \
    --preload \
    --bind 0.0.0.0:8080 {{ project_name }}.wsgi \
    --timeout 360 --workers 5 --max-requests 10000
