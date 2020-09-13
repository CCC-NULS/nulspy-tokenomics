
##### TokenLife Helpful Commands
# npm help config

# npm run serve --port 8089 --verbose

# /usr/node-v12.17.0-linux-x64/lib/node_modules/serve/bin/serve.js -s dist >/dev/null 2>&1

#### To get Running:
cd /usr/share/nginx/html/tokenlife

git pull origin dev99
or
git pull origin master
or whatever github build you want

#### Remove old node cache from last build
rm -rf /usr/share/nginx/html/tokenlife/node_modules/.cache

#### Start
npm run build
  (creates dist dir where everything compiled ends up)

#### Copy top levels up one and the main html dir.  Not sure why but it works.
cd dist
cp -r * ..
sudo cp -r * ../../

#### Use systemctl with sudo to stop and start
sudo systemctl status tokenlifeapp
sudo systemctl stop tokenlifeapp
sudo systemctl start tokenlifeapp


### Plots are in 'static'

### systemctl tokenlifeapp.service does this:
(to serve - this gets run: /usr/node-v12.17.0-linux-x64/lib/node_modules/serve/bin/serve.js)
# /usr/node-v12.17.0-linux-x64/lib/node_modules/serve/bin/serve.js -s dist

###debugging---------------------------------
sudo netstat -anp | grep node

###systemctl-------------------------------------

sudo systemctl status tokenlifeapp
sudo systemctl stop tokenlifeapp
sudo systemctl start tokenlifeapp

###Gunicorn-------------------------------------
Gunicorn runs the python part, connecting it to nginx

gunicorn is built into the systemctl script tokenlife.service:
sudo systemctl status tokenlife

systemctl tokenlife.service does this:
# /home/Nancy/anaconda3/bin/python flask_app.py >/dev/null 2>&1

### To recap:
# tokenlifeapp run the vue flask_app
# tokenlife runs the python part that makes the graph

