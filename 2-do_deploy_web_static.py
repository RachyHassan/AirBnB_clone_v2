#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import put, sudo, env
import os


env.hosts = ['54.236.47.245', '100.26.156.253']
env.user = "ubuntu"


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        archive = archive_path.split('/')[-1]
        archive_no_ext = archive.strip('.tgz')
        new_version = "/data/web_static/releases/" + archive_no_ext
        sudo("mkdir -p {}".format(new_version))
        sudo("tar -zxf /tmp/{} -C {}/".format(archive, new_version))
        sudo("rm -f /tmp/{}".format(archive))
        sudo("mv {}/web_static/* {}/".format(new_version, new_version))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(new_version))
        print("New version deployed!")
        return True
    except:
        return False
