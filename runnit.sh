#!/usr/bin/bash

#npm run serve --port 8089 --verbose

#npm help config

/usr/node-v12.17.0-linux-x64/lib/node_modules/serve/bin/serve.js -s dist >/dev/null 2>&1

/home/Nancy/anaconda3/bin/python flask_app.py >/dev/null 2>&1

/usr/node-v12.17.0-linux-x64/lib/node_modules/serve/bin/serve.js -s dist

git pull origin dev7

sudo netstat -anp | grep node

npm run build







