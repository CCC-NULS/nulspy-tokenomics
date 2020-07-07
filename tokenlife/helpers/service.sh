[Unit]
Description=Gunicorn sockfile instance
After=network.target

[Service]
User=Nancy
Group=Nancy

WorkingDirectory=/usr/share/nginx/html/tokenlife
Environment="PATH=/home/Nancy/anaconda3/bin"
ExecStart=/home/Nancy/anaconda3/bin/gunicorn -c /usr/share/nginx/html/tokenlife/gunicsockdir/gunicornsock.config.py flask_app:application

[Install]
WantedBy=multi-user.target

