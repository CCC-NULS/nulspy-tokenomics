
from flask import Flask, request, render_template, render_template_string
from jinja2 import Environment, select_autoescape
import appsupport
from datetime import datetime
from os import path
from waitress import serve
import flask
import os

app = Flask(__name__)

env = Environment(    # jinja2
    # loader=PackageLoader('psu-calc', 'templates'),
    # loader=PackageLoader('psu-calc', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
)


@app.route('/')   # change later
def index():

    return render_template('index.html')  ## has the user entry form


@app.route('/plots', methods=['GET', 'POST', 'HEAD'])
def plots():
    os.chdir("..")
    basename = os.path.abspath(os.curdir)
    # basename = os.path.dirname(app.instance_path)

    timestp = format(datetime.now(), '%d%H%M%S')
    plotsvg = "plot" + timestp + ".svg"
    plotsdir = 'plotfiles'
    plotfilep = os.path.join(basename, plotsdir)
    plotfilepath = os.path.normcase(plotfilep)

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
                 "plotfilepath": plotfilepath,
                 "plotsvg": plotsvg}

    tk_obj = appsupport.AppSupport()
    tk_obj.main(args_dict)

    with open(plotfilepath) as tfile:
        pfile_contents = tfile.read()
    return render_template_string(pfile_contents)


if __name__ == '__main__':
    serve(app)

    #app.run('127.0.0.1', 5000, debug=True)  (nginx?)

