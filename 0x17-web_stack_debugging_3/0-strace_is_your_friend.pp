# 0. Strace is your friend

exec { 'fix_wordpress':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin:/usr/bin',
}
