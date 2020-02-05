#

from waitress import serve
from time import sleep
from os import path
from flask import Flask, request, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
from datetime import datetime

from app_support_code import nocache
from app_support_code import AppSupport as ac
#sys.stderr = sys.stdout   rootloglev = 40


app = Flask(__name__)
env = Environment(    # jinja2
    loader=PackageLoader('psu-calc', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
)

@app.route('/index', methods = ['POST', 'GET', 'HEAD'])
def index():  # git name of url, construct names and pages, present page with button to next step

    name = request.form['initial']  # from index.html   # the site
    name = request.form['name']  # from index.html   # the site
    name = request.form['name']  # from index.html   # the site
    name = request.form['name']  # from index.html   # the site
    name = request.form['name']  # from index.html   # the site
    print("----------------------------------------------------")
    print("Starting over. site is: ", name)
    sleep(2)
    return render_template('indexn.html', name = name)  ## has a form


if __name__ == '__main__':
    serve(app)
    #app.run('127.0.0.1', 5000, debug=True)
