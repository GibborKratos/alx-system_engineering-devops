exec { 'kill_process':
  command     => 'pkill -f killmenow',
  refreshonly => true,
  subscribe   => Exec['start_my_process'],
}

exec { 'start_my_process':
  command => 'your_command_to_start_killmenow_process',
  onlyif  => 'pgrep -f killmenow',
}

