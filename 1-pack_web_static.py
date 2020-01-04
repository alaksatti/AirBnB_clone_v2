#!/usr/bin/python3
# Fabric script that creates a .tgz acrhive from web_static folder contents
from fabric.api import local
from datetime import datetime
from os.path import exists


def do_pack():
    """creates a .tgz archive from web_static contents"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    path = 'versions/web_static_' + time + '.tgz'
    local('mkdir -p versions')
    local('tar cvfz ' + path + ' web_static')
    if exists(path):
        return path
    return None
