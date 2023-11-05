#!/usr/bin/env bash

cp ./systemd/*.{service,path} /etc/systemd/system/

systemctl daemon-reload

systemctl enable deploy-caddy.{path,service}
systemctl enable princetonpy.service
systemctl start deploy-caddy.{path,service}
systemctl start princetonpy.service
