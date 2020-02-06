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
    initial_supply = request.form['initial_supply']  # from index.html   # the site
    stop_inflation = request.form['stop_inflation']  # from index.html   # the site
    deflation_ratio = request.form['deflation_ratio']  # from index.html   # the site
    annual_inflation = request.form['annual_inflation']  # from index.html   # the site
    inflation_intervals = request.form['start_inflation']  # from same place
    timestp = format(datetime.now(), '%d%H%M%S')

    args_dict = {"ini_sup": initial_supply,
                 "stop_i": stop_inflation,
                 "defl": deflation_ratio,
                 "ann_inf": annual_inflation,
                 "inf_interval": inflation_intervals,
                 "timestp": timestp}

    print("got these", initial_supply, stop_inflation, deflation_ratio, annual_inflation,
          inflation_intervals)

    tokencalc = app_support.app_support()
    fname = tokencalc.main(args_dict)
    img_url = "<img src=" + fname + ">"
    nowplot(img_url)


@app.route('/plot', methods=['GET', 'POST'])
def nowplot(img_url):
    return render_template('plot.html', data=img_url)  ## has the user entry form

#
#
#
#
# @app.route('/')
# def index():
#     return render_template('../templates/index.html')  ## has a form
#
#
# @app.route('/indexn', methods=['POST', 'GET', 'HEAD'])
# def indexn():  # git name of url, construct names and pages, present page with button to next step
#     name = request.form['name']  # from index.html   # the site
#
#     initial_supply = request.form['initial_supply']  # from index.html   # the site
#     stop_inflation = request.form['stop_inflation']  # from index.html   # the site
#     deflation_ratio = request.form['deflation_ratio']  # from index.html   # the site
#     annual_inflation = request.form['annual_inflation']  # from index.html   # the site
#     interval_inflation_rate = annual_inflation / 12  # 5,000,000 NULS
#     start_inflation = 2 * 12
#
#     print("got these", initial_supply, stop_inflation, deflation_ratio, annual_inflation,
#           interval_inflation_rate, start_inflation)
#
#     return render_template('indexn.html', name=initial_supply)  ## has a form



if __name__ == '__main__':
    serve(app)




    #app.run('127.0.0.1', 5000, debug=True)

#>>> from jinja2 import Template
# >>> template = Template('Hello {{ name }}!')
# >>> template.render(name='John Doe')
# u'Hello John Doe!'