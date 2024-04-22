#!/usr/bin/env puppet
# SSH config (puppet)

file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/sshd_config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication.*',
  ensure  => present,
}

file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#?\s*IdentityFile.*',
  ensure  => present,
}
