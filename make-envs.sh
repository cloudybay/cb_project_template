#!/bin/bash

# These ENVs are defined by .gitlab-ci.yml
echo "OPERATION_MODE=$DEPLOY_ENV" >> ./.env
echo "CONTAINER_IMAGE=$CONTAINER_IMAGE" >> ./.env
echo "COMPOSE_PROFILES=$DEPLOY_ENV" >> .env
echo "BASE_DIR=/app" >> .env
echo "SECRET_KEY=$(openssl rand -base64 40)" >> .env
echo "DJANGO_SETTINGS_MODULE={{ project_name }}.settings" >> .env

# 這裡要放這個專案所需要的環境變數，
# 並且要在 Gitlab CI settings -> CI / CD -> Variables 設定實際的環境變數
cat "$ENV_FILE" >> ./.env
