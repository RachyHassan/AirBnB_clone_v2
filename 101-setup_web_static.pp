# A Bash script that sets up your web servers for the deployment
# of web_static

package {'nginx':
  ensure  => installed,
}

exec {'update/upgrade':
  command  => 'sudo apt-get -y update; sudo apt-get upgrade',
  provider => shell,
}

exec {'mkdir':
  command  => 'mkdir -p /data/web_static/releases/test/ 
  /data/web_static/shared/',
  provider => shell,
}

file {'/var/www/html/error_404.html':
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
  content => $content,
}

exec {'symbolicLink':
  command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => shell,
}

exec {'chown':
  command  => 'chown -R "ubuntu:ubuntu" /data/',
  provider => shell,
}

exec {'copy':
  command  => 'cp -a /etc/nginx/sites-available/default{,.orig}',
  provider => shell,
}

$config_file="server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By ${HOSTNAME};
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
  content => $config_file,
}

exec {'restart':
  command  => 'service nginx restart',
  provider => shell,
}
