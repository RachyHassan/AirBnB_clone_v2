#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import put, run, env
import os


# (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
env.hosts = ['54.236.47.245', '100.26.156.253']
env.user = "ubuntu"


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if os.path.exists(archive_path):
        put(archive_path, "/tmp/")
        archive = archive_path.split('/')[-1]
        archive_no_ext = archive.split('.')[0]
        new_version = "/data/web_static/releases/" + archive_no_ext
        run("sudo mkdir -p {}".format(new_version))
        run("sudo tar -zxf /tmp/{} -C {}/".format(archive, new_version))
        run("sudo rm -f /tmp/{}".format(archive))

        # run("sudo mv {}/web_static/* {}".format(new_version, new_version))
        # run("sudo rm -rf {}/web_static".format(new_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(new_version))
        print("New version deployed!")
        return True
    return False
