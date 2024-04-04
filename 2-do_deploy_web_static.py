#!/usr/bin/python3
"""
A Fabric script that distributes an archive to your web servers.
"""
from fabric.api import env, put, run
from os.path import exists
from datetime import datetime
env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'
env.key_filename = '/path/to/your/private/key'


def do_deploy(archive_path):
    """
    A script that distributes an archive to the web servers

    Args:
        archive_path (str): The path to the archive to deploy.

    Returns:
        bool: True if all operations were successful, False otherwise.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/
        filename = archive_path.split('/')[-1].split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(filename))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
            .format(filename, filename))

        # Remove the archive from the web server
        run('rm /tmp/{}.tgz'.format(filename))

        # Move the contents of the extracted folder to its parent directory
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'
            .format(filename, filename))

        # Remove the empty web_static directory
        run('rm -rf /data/web_static/releases/{}/web_static'.format(filename))

        # Update the symbolic link
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(filename))

        return True
    except Exception as e:
        print(e)
        return False
