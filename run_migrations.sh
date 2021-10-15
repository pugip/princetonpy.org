#!/usr/bin/env bash

# shellcheck disable=SC2034
PYTHONPATH=./app
dotenv -f .env.local run -- \
poetry run ./app/manage.py makemigrations
dotenv -f .env.local run -- \
poetry run ./app/manage.py migrate
