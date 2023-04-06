#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static folder
from fabric.api import local
from datetime import datetime as dt


def do_pack():
    ''' archive generator func'''
    try:

        date = dt.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")

        local(f"tar -czvf versions/web_static_{date}.tgz web_static/")

        return f'versions/web_static_{date}.tgz'
    except Exception:
        return None
