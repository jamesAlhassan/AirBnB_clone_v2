#!/usr/bin/env bash
#Sets up your web servers for the deployment of web_stati

#package repo update, install nginx & firewall config
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow "Nginx HTTP"
