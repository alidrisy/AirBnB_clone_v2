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
    list1 = list(reversed(list1))
    for i in range(number, len(list1)):
        print(list1[i])

    list1 = run("ls -r /data/web_static/releases/").split()
    list1 = [a for a in list1 if "web_static_" in a]
    for i in range(number, len(list1)):
        print(list1[i])
