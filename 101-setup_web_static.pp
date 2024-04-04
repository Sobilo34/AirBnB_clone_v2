# Puppet manifest to setup web servers for web_static deployment

# Create the /data/ directory if it doesn't exist
file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create the /data/web_static/ directory if it doesn't exist
file { '/data/web_static':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

# Create the /data/web_static/releases/ directory if it doesn't exist
file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

# Create the /data/web_static/shared/ directory if it doesn't exist
file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

# Create the /data/web_static/releases/test/ directory if it doesn't exist
file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

# Create a fake HTML file /data/web_static/releases/test/index.html
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
}

# Create a symbolic link /data/web_static/current linked to /data/web_static/releases/test/
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}# Puppet manifest to setup web servers for web_static deployment

# Create the /data/ directory if it doesn't exist
file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create the /data/web_static/ directory if it doesn't exist
file { '/data/web_static':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

# Create the /data/web_static/releases/ directory if it doesn't exist
file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

# Create the /data/web_static/shared/ directory if it doesn't exist
file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

# Create the /data/web_static/releases/test/ directory if it doesn't exist
file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

# Create a fake HTML file /data/web_static/releases/test/index.html
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
}

# Create a symbolic link /data/web_static/current linked to /data/web_static/releases/test/
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}
