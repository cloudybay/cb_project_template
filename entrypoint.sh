#!/bin/bash
set -e

# python3 bin/wd_timedrived.py -d
# python3 bin/wd_filedrived.py -d

gunicorn \
    --preload \
    --bind 0.0.0.0:8080 wd.wsgi \
    --timeout 360 --workers 5 --max-requests 10000
