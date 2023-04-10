#!/usr/bin/python3
'''distributes an archive to your web servers, using the function do_deploy:'''
from fabric.api import put, run, env
from os.path import exists


env.hosts = ["100.25.22.118", "52.90.13.68"]


def do_deploy(archive_path):
    '''distributes an archive to your web servers, using do_deploy '''
    if exists(archive_path) is False:
        rerurn False
    file = (archive_path.split('/')[-1]).split('.')[0]
    path = '/data/web_static/releases/' + "{}".format(file)
    tmp = '/tmp/' + file

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(path))
        run("sudo tar -xzf {} -C {}/".format(tmp, path))
        run("sudo rm {}".format(tmp))
        run("sudo mv {}/web_static/* {}/".format(path, path))
        run("sudo rm -rf {}/web_static".format(path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}/ /data/web_static/current".format(path))

        return True

    except:
        return False
