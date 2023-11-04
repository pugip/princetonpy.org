#!/usr/bin/env bash

systemctl disable deploy-caddy.{path,service}
systemctl disable deploy-princetonpy.{path,service}
systemctl disable princetonpy-cron.service
systemctl disable princetonpy-web.service
# rm ./systemd/deploy-caddy.{path,service}