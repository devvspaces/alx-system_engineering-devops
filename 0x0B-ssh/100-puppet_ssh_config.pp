# Ensure that ssh does not use password
include stdlib

file_line { 'ssh password authentication':
  ensure => present,
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication',
  path   => '/etc/ssh/ssh_config'
}

file_line { 'ssh identity key':
  ensure => present,
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^IdentityFile',
  path   => '/etc/ssh/ssh_config'
}

