
exec { 'kill process':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
