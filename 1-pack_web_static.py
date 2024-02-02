#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Packs the web_static folder"""
    # web_static_<year><month><day><hour><minute><second>.tgz
    today_date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "web_static_" + today_date + ".tgz"
    try:
        local('mkdir -p versions/')
        local("tar -zcvf {} versions/".format(filename))
    except Exception:
        return None
