#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static folder
from fabric.api import local
from time import strftime
from datetime import datetime as dt


def do_pack():
    ''' archive generator func'''
    now = dt.now()
    name = now.strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")

        local(f"tar -czvf versions/web_static_{name}.tgz web_static/")

        return f'versions/web_static_{name}.tgz'
    except Exception:
        return None
