#!/usr/bin/python3
from fabric.api import local
from time import strftime


def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    name = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local(f"tar -czvf versions/web_static_{name}.tgz web_static/")

        return f"versions/web_static_{name}.tgz")

    except Exception as e:
        return None
