#!/usr/bin/env bash

</home/princeton/ghtoken docker login ghcr.io --username mhadam --password-stdin
/usr/bin/docker pull ghcr.io/pugip/princetonpy.org/web:release
/usr/bin/docker pull ghcr.io/pugip/princetonpy.org/cron:release