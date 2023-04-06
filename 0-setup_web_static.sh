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

#index.html using tee as sudo doesn't redirect
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    <h1> Devops is Fun </h1>
  </body>
</html>"  | sudo tee data/web_static/releases/test/index.html

#symlink
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

