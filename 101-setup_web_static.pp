# sets up web servers for the deployment of web_static.

 exec { 'update system':
         command => 'apt-get -y update',
         provider => 'shell'
 }

 package { 'nginx':
         ensure => 'installed',
         require => Exec['update system']
 }

 file { '/data/web_static/releases/test/':
	 ensure => 'directory',
	 owner  => 'ubuntu',
	 group  => 'ubuntu'
 }

 file { '/data/web_static/shared/':
	 ensure => 'directory',
	 owner  => 'ubuntu',
	 group  => 'ubuntu'
 }

 file { '/data/web_static/releases/test/index.html':
	 ensure => 'file',
	 content => 'Holberton School',
	 owner  => 'ubuntu',
         group  => 'ubuntu'
 }

 exec {'redirect_me':
         command => 'ln -sf /data/web_static/releases/test /data/web_static/current',
         provider => 'shell'
 }

 exec {'HTTP header':
         command => 'sudo sed -i "38i\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default',
         provider => 'shell'
 }

 service {'nginx':
         ensure => running,
         require => Package['nginx']
 }
