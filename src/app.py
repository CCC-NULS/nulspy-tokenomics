#!venv
# from time import sleep

from waitress import serve
from flask import Flask, request, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
import app_support
from datetime import datetime

app = Flask(__name__)
env = Environment(    # jinja2
    # loader=PackageLoader('psu-calc', 'templates'),
    # loader=PackageLoader('psu-calc', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
)


@app.route('/')   # change later
def index():
    return render_template('index.html')  ## has the user entry form


@app.route('/show',  methods=['POST', 'GET', 'HEAD'])
def show():
    timestp = format(datetime.now(), '%d%H%M%S')
    fname = "plots/plot" + timestp + ".svg"
    img_url = "<img src=" + fname + ">"

    initial_supply = request.form['initial_supply']  # from index.html   # the site
    stop_inflation = request.form['stop_inflation']  # from index.html   # the site
    deflation_ratio = request.form['deflation_ratio']  # from index.html   # the site
    annual_inflation = request.form['annual_inflation']  # from index.html   # the site
    inflation_intervals = request.form['start_inflation']  # from same place

    args_dict = {"ini_sup": initial_supply,
                 "stop_i": stop_inflation,
                 "defl": deflation_ratio,
                 "ann_inf": annual_inflation,
                 "inf_interval": inflation_intervals,
                 "timestp": timestp,
                 "fname": fname }

    tk_obj = app_support.app_support()
    tk_obj.main(args_dict)
    nowplot(img_url)


@app.route('/plot', methods=['GET', 'POST'])
def nowplot(img_url):
    return render_template('plot.html', data=img_url)


if __name__ == '__main__':
    serve(app)


    #app.run('127.0.0.1', 5000, debug=True)  (nginx?)

