#!/usr/bin/env bash

systemctl disable deploy-caddy.{path,service}
systemctl disable princetonpy.service
systemctl daemon-reload
# rm ./systemd/deploy-caddy.{path,service}