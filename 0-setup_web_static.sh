#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment
# of web_static

if [[ ! $(command -v nginx) ]]; then
    apt-get install -y nginx
fi
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Ceci n'est pas une page" > /var/www/html/error_404.html

content="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo "$content" > /data/web_static/releases/test/index.html

# A symbolic link /data/.../current linked to /data/.../test/ folder
ln -sfn /data/web_static/releases/test/ /data/web_static/current

chown -R "ubuntu":"ubuntu" /data/
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

        server_name dobodo.tech;

        location / {
                try_files \$uri \$uri/ =404;
        }

        location /hbnb_static {
                alias /data/web_static/current/;
        }
}"

echo "${config_file}" > /etc/nginx/sites-enabled/default
service nginx restart
