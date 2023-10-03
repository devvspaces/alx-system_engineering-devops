# this installs nginx and configures it to serve a static page

exec { 'apt-get update':
  command => 'apt-get update',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get update']
}

service { 'nginx':
  ensure  => 'running',
  enable  => 'true',
  require => Package['nginx']
}

file { 'create a index.html file':
  ensure  => 'present',
  path    => '/var/www/html/index.html',
  content => 'Hello World!'
}


$nginx_conf = 'server {
  listen 80 default_server;
  listen [::]:80 default_server ipv6only=on;

  root /var/www/html;
  index index.html index.htm;

  server_name localhost;

  location /redirect_me {
    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
  }

  location / {
    try_files $uri $uri/ =404;
  }

  error_page 404 /404.html;
}'

file { 'nginx.conf':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  content => $nginx_conf,
  require => Package['nginx'],
  notify  => Service['nginx']
}
