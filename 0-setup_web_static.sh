#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment
# of web_static

apt-get -y update
apt-get -y upgrade
apt-get -y install nginx

mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "This is not a page" > /var/www/html/error_404.html

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Creating a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R "ubuntu:ubuntu" /data/
cp -a /etc/nginx/sites-available/default{,.orig}

# Update the Nginx configuration to serve the content
# of /data/web_static/current/ to hbnb_static
config_file="server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By $HOSTNAME;
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

echo "${config_file}" > /etc/nginx/sites-available/default
# Restart nginx
service nginx restart
