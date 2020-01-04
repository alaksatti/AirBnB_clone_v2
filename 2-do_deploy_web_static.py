#!/usr/bin/python3
# Fabric script that distributes archive to remote server
from fabric.api import local, env, put, run
from datetime import datetime
from os.path import exists, isfile
env.hosts = ['35.196.198.246', '34.73.64.187']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/holberton'


def do_pack():
    """creates a .tgz archive from web_static contents"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    path = 'versions/web_static_' + time + '.tgz'
    local('mkdir -p versions')
    local('tar cvfz ' + path + ' web_static')
    if exists(path):
        return path
    return None


def do_deploy(archive_path):
    'deploy archive to web servers'
    if not exists(archive_path) and not isfile(archive_path):
        return False
    try:
        put(archive_path, '/tmp')
        name = archive_path.split('/')[1][:-4]
        run('sudo mkdir -p /data/web_static/releases/' + name + '/')
        run('sudo chown -R ubuntu:ubuntu /data')
        run('tar -xzf /tmp/' + name + '.tgz'
            ' -C /data/web_static/releases/' + name + '/')
        run('rm /tmp/' + name + '.tgz')
        run('mv /data/web_static/releases/' + name + '/web_static/* ' +
            '/data/web_static/releases/' + name + '/')
        run('rm -rf /data/web_static/releases/' + name + '/web_static')
        run('rm -rf /data/web_static/current')
        run('ln -sf /data/web_static/releases/' + name + '/ ' +
            '/data/web_static/current')
        print("New version deployed!")
    except:
        return False
    return True
