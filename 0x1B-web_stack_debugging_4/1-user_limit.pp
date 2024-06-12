# Changes the OS configuration so that it is possible to login 
# with the holberton user and open a file without any error message.
exec { 'change-os-configuration-for-holberton-user':
  command => '/usr/bin/env sudo sed -i "s/# End of file/\\nholberton hard nofile 4096\\nholberton soft nofile 1024\\n# End of file/" /etc/security/limits.conf',
}

