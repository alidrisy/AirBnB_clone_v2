#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
from fabric.api import local
from datetime import datetime

def do_pack():
    """ generates a .tgz archive from the contents of the web_static folder 
    of your AirBnB Clone repo, using the function do_pack."""
    t = datetime.now()
    name = f"web_static_{t.year}{t.month}{t.day}{t.hour}{t.minute}\
{t.second}.tgz"
    local("mkdir -p versions")
    com = local(f"tar -cvzf versions/{name} web_static")
    if com.failed is True:
        return (None)
    return (archive_path)
