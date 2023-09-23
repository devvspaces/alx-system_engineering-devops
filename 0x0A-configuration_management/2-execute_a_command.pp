# This is a sample file to show how to use the exec resource

exec { 'kill process':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
