#!/bin/bash
set -e

cp -f ./conf/$OPERATION_MODE/nginx.conf /etc/nginx/conf.d/default.conf

./wait-for-it.sh app:8080 -t 30 -- nginx -g 'daemon off;'

exec "$@"