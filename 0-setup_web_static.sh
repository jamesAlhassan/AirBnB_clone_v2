#!/usr/bin/env bash
# script sets up web servers for deployment of web_static

# Check for nginx. If not installed, install and configure
sudo apt-get update;
sudo apt-get install nginx;
sudo ufw allow 'Nginx HTTP'

# check and create directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# create index.html file and add html content
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# create symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# give ownership of data to ubuntu
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/; }' /etc/nginx/sites-enabled/default

sudo service nginx restart
