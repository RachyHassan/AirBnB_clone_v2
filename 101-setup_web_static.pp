# A Bash script that sets up your web servers for the deployment
# of web_static

package {'nginx':
  ensure  => installed,
}

exec {'update/upgrade':
  command  => 'sudo apt-get -y update; sudo apt-get upgrade',
  provider => shell,
}

file {'/data':
  ensure => directory,
}
file {'/data/web_static/':
  ensure => directory,
}
file {'/data/web_static/releases/':
  ensure => directory,
}
file {'/data/web_static/releases/test/':
  ensure => directory,
}
file {'/data/web_static/shared/':
  ensure => directory,
}

file {'/var/www/html/error_404.html':
  ensure  => present,
  content => 'Ceci n\'est pas une page',
}

$content="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

file {'/data/web_static/releases/test/index.html':
  ensure  => present,
  content => $content,
}

file {'/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
}

exec {'chown':
  command  => 'sudo chown -R "ubuntu:ubuntu" /data/',
  provider => shell,
}

# exec {'copy':
#  command  => 'cp -a /etc/nginx/sites-available/default{,.orig}',
# provider => shell,
# }

$config_file="server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By ${facts['networking']['hostname']};
        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        error_page 404 /error_404.html;

        root /var/www/html;

        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                try_files \$uri \$uri/ =404;
        }

        location /hbnb_static {
                alias /data/web_static/current/;
        }
}"

file {'/etc/nginx/sites-available/default':
  ensure  => present,
  content => $config_file,
}

service {'nginx':
  ensure => running,
}
