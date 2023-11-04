#!/usr/bin/env bash

cp ./systemd/*.{service,path} /etc/systemd/system/

systemctl daemon-reload

systemctl enable deploy-caddy.{path,service}
systemctl enable princetonpy-cron.service
systemctl enable princetonpy-web.service
systemctl start deploy-caddy.{path,service}
systemctl start princetonpy-cron.service
systemctl start princetonpy-web.service
