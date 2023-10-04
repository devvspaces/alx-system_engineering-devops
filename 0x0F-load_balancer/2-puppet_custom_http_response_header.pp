# Configure Nginx to serve a static page

exec { 'update packages':
  command => 'apt-get update',
  path    => ['/usr/local/sbin','/usr/local/bin','/usr/sbin','/usr/bin','/sbin','/bin']
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update packages']
}

exec { 'allow Nginx http':
  command => "ufw allow 'Nginx HTTP'",
  path    => ['/usr/local/sbin','/usr/local/bin','/usr/sbin','/usr/bin','/sbin','/bin']
}

exec { 'mkdir www/html folder':
  command => 'mkdir -p /var/www/html',
  path    => ['/usr/local/sbin','/usr/local/bin','/usr/sbin','/usr/bin','/sbin','/bin']
}

file { '/var/www/html/index.html':
  content => "Hello World!\n",
  require => Exec['mkdir www/html folder']
}

file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
  require => Exec['mkdir www/html folder']
}

exec { 'chmod www folder':
  command => 'chmod -R 755 /var/www',
  path    => ['/usr/local/sbin','/usr/local/bin','/usr/sbin','/usr/bin','/sbin','/bin'],
  require => Exec['mkdir www/html folder']
}

file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
"server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;
    server_name _;
    add_header X-Served-By \$hostname;

    location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.
        try_files \$uri \$uri/ =404;
    }

    error_page 404 /404.html;

    location  /404.html {
        internal;
    }
    
    if (\$request_filename ~ redirect_me){
        rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
    }
}
",
  require => Package['nginx'],
  notify  => Exec['restart service'],
}

exec { 'restart service':
  command => 'service nginx restart',
  path    => ['/usr/local/sbin','/usr/local/bin','/usr/sbin','/usr/bin','/sbin','/bin'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
