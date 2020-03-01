#!/bin/bash

##  nohup 2>&1 uwsgi --socket 0.0.0.0:5002 --protocol=http -w wsgi &

nohup uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi &> /var/log/psu/nohup.log &

##  nohup uwsgi --socket 0.0.0.0:5002 --protocol=http -w wsgi &> /var/log/psu/nohup.log &

