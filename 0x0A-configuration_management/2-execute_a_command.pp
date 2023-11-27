class killmenow {
  exec { 'killmenow_process':
    command     => '/usr/bin/pkill killmenow',
    refreshonly => true,
    onlyif      => '/usr/bin/pgrep killmenow',
  }
}

include killmenow

