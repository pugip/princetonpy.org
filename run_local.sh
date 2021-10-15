#!/usr/bin/env bash

# shellcheck disable=SC2034
PYTHONPATH=./app
hypercorn princetonpy.asgi:application --bind 0.0.0.0:8000
