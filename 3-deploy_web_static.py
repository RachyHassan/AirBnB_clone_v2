#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import put, run, env, local
from datetime import datetime
import os


# (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
env.hosts = ['54.236.47.245', '100.26.156.253']
env.user = "ubuntu"


def do_pack():
    """Packs the web_static folder into a tgz file"""

    today_date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_" + today_date + ".tgz"
    try:
        local('mkdir -p versions/')
        local("tar -zcvf {} web_static/".format(filename))
        return filename
    except Exception:
        return None


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
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(new_version))
        print("New version deployed!")
        return True
    return False


def deploy():
    """Packs and Deploys the website in one file"""
    archive_path = do_pack()
    if bool(archive_path):
        return do_deploy(archive_path=archive_path)
    else:
        return False
