#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static folder

from fabric.api import *
from time import strftime as st
from datetime import datetime as dt


def do_pack():
    ''' archive generator func'''
    now = dt.now()
    name = st('%Y%m%d%H%M%S')

    try:
        local('mkdir -p versions')

        local(f'tar -cfvz versions/web_static_{name}.tgz')

        return f'versions/web_static_{name}.tgz'
    except Exception:
        return None
