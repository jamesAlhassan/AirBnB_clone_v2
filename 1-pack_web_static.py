#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static folder

from fabric.api import local
from datetime import datetime as dt


def do_pack():
    ''' archive generator func'''
    local("sudo mkdir -p versions")
    date = dt.now().strftime("%Y%m%d%H%M%S")
    filename = f"versions/web_static_{date}.tgz"
    result = local("sudo tar -cvzf {filename} web_static")
    if result.succeeded:
        return filename
    else:
        return None
