#!/usr/bin/python3

"""Script (based on the file 1-pack_web_static.py) that distributes
    an archive to your web servers, using the function do_deploy
"""

from fabric.api import env, put, run
import os

env.hosts = [
            '107.23.100.114',
            '35.153.17.86'
        ]

env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """Function to distribute an archive to web servers
    """
    if not os.path.exists(archive_path):
        return (False)

    archive_name = archive_path.split('/')[-1]
    name = archive_name.split('.')[0]
    uncompress_path = "/data/web_static/releases/{}".format(name)
    uncompress_cmd = "sudo tar -xzf /tmp/{} -C {}"\
                     .format(archive_name, uncompress_path)
    create_path = "sudo mkdir -p {}".format(uncompress_path)
    remove_archive = "sudo rm -rf /tmp/{}".format(archive_name)
    move = "sudo mv {}/web_static/* {}"\
           .format(uncompress_path, uncompress_path)
    remove_web_static = "sudo rm -rf {}/web_static".format(uncompress_path)
    link_archive = "sudo ln -s {} /data/web_static/current"\
                   .format(uncompress_path)

    if put(archive_path, '/tmp/').failed is True:
        return (False)
    if run(create_path).failed is True:
        return (False)
    if run(uncompress_cmd).failed is True:
        return (False)
    if run(remove_archive).failed is True:
        return (False)
    if run(move).failed is True:
        return (False)
    if run(remove_web_static).failed is True:
        return (False)
    if run("sudo rm -rf /data/web_static/current").failed is True:
        return (False)
    if run(link_archive).failed is True:
        return (False)
    print("New version deployed!")
    return (True)
