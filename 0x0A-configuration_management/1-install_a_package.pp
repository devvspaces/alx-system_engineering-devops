# this installs flask

exec { 'apt-get update':
  command => 'apt-get update',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}

package { 'python3-pip':
  ensure  => 'installed',
  require => Exec['apt-get update']
}

exec { 'flask':
  command => 'pip3 install flask==2.1.0',
  require => Package['python3-pip'],
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
