#Increase the amount of traffic Nginx server can handle
exec { 'change-request-limit':
  command => '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx',
}

exec { 'restart-nginx-service':
  command     => '/usr/bin/env service nginx restart',
  refreshonly => true,
  subscribe   => Exec['change-request-limit'],
}
