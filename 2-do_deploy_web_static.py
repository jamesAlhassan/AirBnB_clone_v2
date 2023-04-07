#!/usr/bin/python3
'''distributes an archive to your web servers, using the function do_deploy:'''
from fabric.api import put, run, env
from datetime import datetime as dt

env.hosts = ["100.25.22.118", "52.90.13.68"]


def do_deploy(archive_path):
    '''distributes an archive to your web servers, using do_deploy '''
    if (not archive_path):
        rerurn False
    file = (archive_path.split('/')[-1]).split('.')[0]
    path = '/data/web_static/releases/' + "{}".format(file)
    tmp = '/tmp/' + file

    put(archive_path, '/tmp/')
    run('mkdir -p {}/'.format(path))
    run('tar -xzf {} -C {}/'.format(tmp, path))
    run('rm {}'.format(tmp))
