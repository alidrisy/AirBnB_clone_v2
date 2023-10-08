#!/usr/bin/python3
""" Fabric script that generates a .tgz archive  and distributes it
to server """
from fabric.api import put, run, env
from datetime import datetime
import os

env.hosts = ["107.23.100.114", "35.153.17.86"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """ distributes an archive to your web servers """

    if not os.path.exists(archive_path):
        return (False)

    dir1 = archive_path.split("/")[-1].split(".")[0]
    file1 = f"{dir1}.tgz"
    path = "/data/web_static/releases/{}".format(dir1)

    check = put(archive_path, "/tmp/")
    if check.failed is True:
        return (False)
    check = run(f"sudo mkdir -p {path}")
    if check.failed is True:
        return (False)
    check = run(f"sudo tar -xzf /tmp/{file1} -C {path}")
    if check.failed is True:
        return (False)
    check = run(f"sudo rm -rf /tmp/{file1}")
    if check.failed is True:
        return (False)
    check = run(f"sudo mv {path}/web_static/* {path}")
    if check.failed is True:
        return (False)
    check = run(f"sudo rm -rf {path}/web_static/")
    if check.failed is True:
        return (False)
    check = run(f"sudo rm -rf /data/web_static/current")
    if check.failed is True:
        return (False)
    check = run(f"sudo ln -s {path} /data/web_static/current")
    if check.failed is True:
        return (False)
    return (True)
