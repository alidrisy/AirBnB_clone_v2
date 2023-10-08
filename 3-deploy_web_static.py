#!/usr/bin/python3
""" Fabric script that generates a .tgz archive  and distributes it
to server """
from fabric.api import put, run, env, local
from datetime import datetime
import os

env.hosts = ["107.23.100.114", "35.153.17.86"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


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
    check = run(f"mkdir -p {path}")
    if check.failed is True:
        return (False)
    check = run(f"tar -xzf /tmp/{file1} -C {path}")
    if check.failed is True:
        return (False)
    check = run(f"rm -rf /tmp/{file1}")
    if check.failed is True:
        return (False)
    check = run(f"mv {path}/web_static/* {path}")
    if check.failed is True:
        return (False)
    check = run(f"rm -rf {path}/web_static")
    if check.failed is True:
        return (False)
    check = run(f"rm -rf /data/web_static/current")
    if check.failed is True:
        return (False)
    check = run(f"ln -s {path} /data/web_static/current")
    if check.failed is True:
        return (False)
    return (True)


def deploy():
    """Creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
