# Create a file with the content "I love Puppet" and the permissions 0744

file { 'create a file':
  ensure  => 'present',
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  mode    => '0744'
}
