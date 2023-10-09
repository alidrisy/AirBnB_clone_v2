# sets up web servers for the deployment of web_static.

 exec { 'update system':
         command => 'apt-get -y update',
         provider => 'shell'
 }

 package { 'nginx':
         ensure => 'installed',
         require => Exec['update system']
 }

 file { '/data':
	 ensure  => 'directory' 
 } -> 
  
 file { '/data/web_static':
	 ensure => 'directory' 
 } -> 
  
 file { '/data/web_static/releases':
	 ensure => 'directory' 
 } -> 
  
 file { '/data/web_static/releases/test':
	 ensure => 'directory' 
 } -> 
  
 file { '/data/web_static/shared':
	 ensure => 'directory' 
 } -> 
  
 file { '/data/web_static/releases/test/index.html':
	 ensure  => 'present',
	 content => "Holberton School\n" 
 } -> 
  
 file { '/data/web_static/current':
	 ensure => 'link',
	 target => '/data/web_static/releases/test' 
 } ->

 exec { 'chown -R ubuntu:ubuntu /data/':
	 path => '/usr/bin/:/usr/local/bin/:/bin/' 
 } ->
 
 exec {'new_location':
         command => 'sed -i "38i\	location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default',
         provider => 'shell'
 }

 service {'nginx':
         ensure => running,
         require => Package['nginx']
 }
