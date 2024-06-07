#creating a custom HTTP header(puppet)
#custom HTTP header must be X-Served-By
#configures an ubuntu machine
exec { '/usr/bin/apt-get -y update': }

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Holberton School!',
}

file_line { 'add header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => '        add_header X-Served-By $hostname;',
  after  => 'server_name _;',
}

service { 'nginx':
  ensure => running,
}
