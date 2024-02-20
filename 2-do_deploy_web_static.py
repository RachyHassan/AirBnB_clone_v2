#!/usr/bin/python3
"""
A fabric Script that distributes an archive to
webservers, using the function do_deploy
"""
from fabric.api import put, sudo, env
import os


env.hosts = ['52.91.132.212', '54.198.58.74']
env.user = "ubuntu"


def do_deploy(archive_path):
    """A function that distributes an archive to web servers"""
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
