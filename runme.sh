#!/bin/bash

nohup 2>&1 uwsgi --socket 0.0.0.0:5002 --protocol=http -w wsgi &


