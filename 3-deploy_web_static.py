#!/usr/bin/python3
"""
A fabric script that creates and distributes an archive
to web servers, using the function deploy
"""
from datetime import datetime
from fabric.api import local
from fabric.operations import put, sudo, env
import os


env.hosts = ['52.91.132.212', '54.198.58.74']
env.user = "ubuntu"


def do_pack():
    """A function that packs the web_static folder into a tgz file"""

    today_date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_" + today_date + ".tgz"
    try:
        local('mkdir -p versions/')
        local("tar -zcvf {} web_static/".format(filename))
        return filename
    except Exception:
        return None


def do_deploy(archive_path):
    """A function that distributes an archive to your web servers"""
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


def deploy():
    """ A function that packs and Deploys the website in one file"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
