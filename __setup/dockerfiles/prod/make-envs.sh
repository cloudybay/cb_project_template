#!/bin/bash

# These ENVs are defined by .gitlab-ci.yml
echo "IMAGE_PROJECT_DIR=$IMAGE_PROJECT_DIR" > ./.env
echo "DOCKER_IMAGE=$CONTAINER_IMAGE" >> ./.env
echo "STAGING_SERVER_PORT=$STAGING_SERVER_PORT" >> ./.env
echo "OPERATION_MODE=prod" >> ./.env


# 這裡要放這個專案所需要的環境變數，
# 並且要在 Gitlab CI settings -> CI / CD -> Variables 設定實際的環境變數
cat "$ENV_FILE" >> ./.env
