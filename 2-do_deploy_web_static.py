#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import put, run, env
import os


# Prototype: def do_deploy(archive_path):
def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    # Returns False if the file at the path archive_path doesn’t exist
    if not os.path.exists(archive_path):
        return False
    # (self) archive path versions/web_static_1983929.tgz
    try:
        # The script should take the following steps:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive filename without extension>
        # on the web server
        archive = archive_path.split('/')[-1]
        archive_no_ext = archive.split('.')[0]
        run(f"mkdir -p /data/web_static/releases/{archive_no_ext}/")
        run(f"tar -zxf /tmp/{archive} -C \
            /data/web_static/releases/{archive_no_ext}/")
        # Delete the archive from the web server
        run(f"rm -f /tmp/{archive}")
        # Delete the symbolic link /data/web_static/current from the web server
        run("rm /data/web_static/current")
        # Create a new the symbolic link /data/web_static/current on the
        # web server, linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)
        run(f"ln -sf /data/web_static/releases/{archive_no_ext}/ \
            /data/web_static/current")
        return True
    except Exception:
        return False
    # Returns True if all operations have been done correctly,
    # otherwise returns False

# All remote commands must be executed on your both web servers
# (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
env.hosts = ['54.236.47.245', '100.26.156.253']