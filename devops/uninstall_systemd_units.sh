#!/usr/bin/env bash

systemctl disable deploy-caddy.{path,service}
systemctl disable deploy-project.{path,service}
systemctl disable project.path
systemctl disable princetonpy-cron.service
systemctl disable princetonpy-web.service
# rm ./systemd/deploy-caddy.{path,service}