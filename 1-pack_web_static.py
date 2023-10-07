#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
from fabric.api import local
from datetime import datetime

def do_pack():
    t = datetime.now()
    name = f"web_static_{t.year}{t.month}{t.day}{t.hour}{t.minute}{t.second}.tgz"
    local("mkdir -p versions")
    local(f"tar -cvzf versions/{name} web_static")
