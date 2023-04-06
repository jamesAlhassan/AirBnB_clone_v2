#!/usr/bin/env bash
#Sets up your web servers for the deployment of web_stati

#package repo update, install nginx & firewall config
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow "Nginx HTTP"

# create dirs
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
