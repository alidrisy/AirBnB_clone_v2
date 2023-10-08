#!/usr/bin/python3
""" Fabric script that generates a .tgz archive  and distributes it
to server """
from fabric.api import run, env, local

env.hosts = ["107.23.100.114", "35.153.17.86"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_clean(number=0):
    """Deletes out-of-date archives"""
    list1 = run("ls -r /data/web_static/releases/").split()
    list1 = [a for a in list1 if "web_static_" in a]
    number = int(number)
    if number == 0:
        number = 1
    for i in range(number, len(list1)):
        run(f"rm -rf /data/web_static/releases/{list1[i]}")
        local(f"rm -rf versions/{list1[i]}")
