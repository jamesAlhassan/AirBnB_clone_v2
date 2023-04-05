#!/usr/bin/env bash
# script sets up web servers for deployment of web_static

# Check for nginx. If not installed, install and configure
if ! command -v nginx &> /dev/null
then
	sudo apt-get update;
	sudo apt-get install nginx;
	sudo ufw allow 'Nginx HTTP'
fi

# check and create directories
[ ! -d "/data/" ] && sudo mkdir /data/
[ ! -d "/data/web_static/" ] && sudo mkdir /data/web_static/
[ ! -d "/data/web_static/releases/" ] && sudo mkdir /data/web_static/releases/
[ ! -d "/data/web_static/shared/" ] && sudo mkdir /data/web_static/shared/
[ ! -d "/data/web_static/releases/test" ] && sudo mkdir /data/web_static/releases/test/

# create index.html file and add html content
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
	<head>
	</head>
	<body>
		Welcome to my Webserver
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# create symbolic link
ln -s -f /data/web_static/releases/test/ /data/web_static/current

# give ownership of data to ubuntu
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location/hbnb_static { alias /data/web_static/current/; }' /etc/nginx/sites-enabled/default

sudo service nginx restart
