#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives.
"""
from fabric.api import env, run, local
from datetime import datetime
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'
env.key_filename = '/path/to/your/private/key'


def do_clean(number=0):
    """
    Deletes out-of-date archives.

    Args:
        number (int): The number of archives to keep. Default is 0.
    """
    # Determine the list of archives to keep
    if int(number) <= 1:
        number_to_keep = 1
    else:
        number_to_keep = int(number)

    # Get the list of archives in the versions folder
    archives = local('ls -1t versions', capture=True).split('\n')

    # Delete unnecessary archives in the versions folder
    for archive in archives[number_to_keep:]:
        local('rm -f versions/{}'.format(archive))

    # Get the list of archives in the releases folder of each web server
    for host in env.hosts:
        releases = run('ls -1t /data/web_static/releases').split('\n')

        # Delete unnecessary archives in the releases folder
        for release in releases[number_to_keep:]:
            run('rm -rf /data/web_static/releases/{}'.format(release))#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives.
"""
from fabric.api import env, run, local
from datetime import datetime
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'
env.key_filename = '/path/to/your/private/key'


def do_clean(number=0):
    """
    Deletes out-of-date archives.

    Args:
        number (int): The number of archives to keep. Default is 0.
    """
    # Determine the list of archives to keep
    if int(number) <= 1:
        number_to_keep = 1
    else:
        number_to_keep = int(number)

    # Get the list of archives in the versions folder
    archives = local('ls -1t versions', capture=True).split('\n')

    # Delete unnecessary archives in the versions folder
    for archive in archives[number_to_keep:]:
        local('rm -f versions/{}'.format(archive))

    # Get the list of archives in the releases folder of each web server
    for host in env.hosts:
        releases = run('ls -1t /data/web_static/releases').split('\n')

        # Delete unnecessary archives in the releases folder
        for release in releases[number_to_keep:]:
            run('rm -rf /data/web_static/releases/{}'.format(release))
