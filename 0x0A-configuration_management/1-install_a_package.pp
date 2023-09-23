exec { 'apt-get update':
  command => '/usr/bin/apt-get update'
}

package { 'python3-pip':
  ensure  => 'installed',
  require => Exec['apt-get update']
}

exec { 'flask':
  command => '/usr/bin/pip3 install flask',
  require => Package['python3-pip']
}
