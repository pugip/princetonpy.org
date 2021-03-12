#!/usr/bin/env bash

CONTAINER_NAME=$(sudo docker container ps -f "name=^princetonpyorg_nginx_." --format="{{.Names}}")
SCRIPT_PATH=$(pwd $(dirname $(readlink -f $0)))
if [ -z "$CONTAINER_NAME" ]; then
  echo "could not find the nginx container"
  exit 1
fi
sudo docker cp "$SCRIPT_PATH"/nginx/pages/. "$CONTAINER_NAME":/var/www/princetonpy.org/pages/