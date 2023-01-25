#!/bin/bash

# These ENVs are defined by .gitlab-ci.yml
echo "OPERATION_MODE=$DEPLOY_ENV" >> ./.env
echo "BACKEND_IMAGE=$CONTAINER_IMAGE" >> ./.env
echo "FRONTEND_IMAGE=$CONTAINER_IMAGE-web" >> ./.env
echo "COMPOSE_PROFILES=$DEPLOY_ENV" >> .env
echo "BASE_DIR=/app" >> .env

# 這裡要放這個專案所需要的環境變數，
# 並且要在 Gitlab CI settings -> CI / CD -> Variables 設定實際的環境變數
cat "$ENV_FILE" >> ./.env
