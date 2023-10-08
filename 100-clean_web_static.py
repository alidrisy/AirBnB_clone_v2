#!/usr/bin/python3
""" Fabric script that generates a .tgz archive  and distributes it
to server """
from fabric.api import run, env, local
import os

env.hosts = ["107.23.100.114", "35.153.17.86"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_clean(number=0):
    """Deletes out-of-date archives"""

    number = int(number)
    if number == 0:
        number = 1

    list1 = sorted(os.listdir("versions"))
    [list1.pop() for i in range(number)]
    [local("rm versions/{}".format(a)) for a in list1]

    list1 = run("ls -tr /data/web_static/releases").split()
    list1 = [a for a in list1 if "web_static_" in a]
    [list1.pop() for i in range(number)]
    [run("rm -rf ./{}".format(a)) for a in list1]
