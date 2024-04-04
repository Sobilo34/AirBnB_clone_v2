#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the
contents of the web_static folder of my AirBnB Clone repo,
using the function do_pack#!/usr/bin/python3
"""


from fabric.api import local
from datetime import datetime


def do_pack():
    """
    A function that creates a .tgz archive

    Returns:
        str: The path to the generated archive if successful, None otherwise.
    """
    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Format the current date and time
    now = datetime.now()
    date_time = now.strftime("%Y%m%d%H%M%S")

    # Compress the web_static folder into a .tgz archive
    archive_name = "versions/web_static_{}.tgz".format(date_time)
    result = local("tar -cvzf {} web_static".format(archive_name))

    if result.failed:
        return None
    else:
        return archive_name
