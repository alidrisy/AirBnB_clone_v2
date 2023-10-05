#!/usr/bin/env bash
# sets up web servers for the deployment of web_static.

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -Rh ubuntu:ubuntu /data/
sudo chmod -R 755 /data/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
se=$(grep "hbnb_static" /etc/nginx/sites-available/default)
if [ -z "$se" ]
then
        sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
fi
sudo service nginx restart
