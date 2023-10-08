#!/usr/bin/python3
""" Fabric script that generates a .tgz archive  and distributes it
to server """
from fabric.api import put, run, env, local, cd
from datetime import datetime
import os

env.hosts = ["107.23.100.114", "35.153.17.86"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_clean(number=0):
    number = int(number)
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        print(archives)
