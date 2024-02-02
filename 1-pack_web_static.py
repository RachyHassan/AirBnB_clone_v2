#!/usr/bin/python3
"""Compress before sending"""

from fabric.api import local
from datetime import datetime


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
