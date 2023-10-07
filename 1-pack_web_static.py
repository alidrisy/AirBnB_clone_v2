#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ generates a .tgz archive from the contents of the web_static folder
    of your AirBnB Clone repo, using the function do_pack."""

    t = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "web_static_{}.tgz".format(t)
    local("mkdir -p versions")
    com = local(f"tar -cvzf versions/{name} web_static")

    if com.failed is True:
        return (None)
    return (f"versions/{name}")
