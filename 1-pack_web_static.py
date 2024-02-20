#!/usr/bin/python3
""" A Fabric script that generates a .tgz archive
from the contents of the web_static folder of AirBnB Clone repo,
using the function do_pack."""

from collections.abc import Mapping
from datetime import datetime
from fabric.api import local


def do_pack():
    """ A function that packs the web_static folder into a tgz file"""

    today_date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_" + today_date + ".tgz"
    try:
        local('mkdir -p versions/')
        local("tar -zcvf {} web_static/".format(filename))
        return filename
    except Exception:
        return None
