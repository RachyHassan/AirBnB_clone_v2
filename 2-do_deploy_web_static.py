#!/usr/bin/python3
"""Compress before sending"""

from fabric.api import put, run, env
import os


env.hosts = ['54.236.47.245', '100.26.156.253']


def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    if not os.path.exists(archive_path):
        return False
    try:
        archive = archive_path.split('/')[-1]
        put(archive_path, f'/tmp/{archive}')
        archive_folder = archive.split('.')
        path = "/data/web_static/releases"
        run("mkdir -p {}/{}/".format(path, archive_folder[0]))
        new_archive = '.'.join(archive_folder)
        run("tar -xzf /tmp/{} -C {}/{}/"
            .format(new_archive, path, archive_folder[0]))
        run("rm /tmp/{}".format(archive))
        run("mv {}/{}/web_static/* {}/{}/"
            .format(path, archive_folder[0], path, archive_folder[0]))
        run("rm -rf {}/{}/web_static".format(path, archive_folder[0]))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}/{} /data/web_static/current"
            .format(path, archive_folder[0]))
        return True
    except Exception:
        return False
