
from flask import Flask, request, render_template, render_template_string
from jinja2 import Environment, select_autoescape
import appsupport
from datetime import datetime
from os import path
from waitress import serve
import flask
import os
from time import sleep

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
    #basename = os.path.abspath(os.curdir)

    basename ='/home/jetgal/psucalc'
    timestp = format(datetime.now(), '%d%H%M%S')
    plotsvg = "plot" + timestp + ".svg"
    plotsdir = 'plotfiles'
    plotfilesdir = os.path.join(basename, plotsdir)
    plotfp = os.path.join(plotfilesdir, plotsvg)
    plotfilepath = os.path.normpath(plotfp)

    initial_supply_y = request.form['initial_supply_y']  # from index.html   # the site
    stop_inflation_y = request.form['stop_inflation_y']  # from index.html   # the site
    disinflation_ratio = request.form['disinflation_ratio']  # from index.html   # the site
    annual_inflation = request.form['annual_inflation']  # from index.html   # the site
    inflation_intervals = request.form['start_inflation']  # from same place

    args_dict = {"initial_supply_y": initial_supply_y,
                 "stop_inflation_y": stop_inflation_y,
                 "disinflation_ratio": disinflation_ratio,
                 "annual_inflation": annual_inflation,
                 "inflation_intervals": inflation_intervals,
                 "timestp": timestp,
                 "plotfilepath": plotfilepath,
                 "plotsvg": plotsvg}

    tk_obj = appsupport.AppSupport()
    tk_obj.main(args_dict)

    filethere = 1
    while filethere:
        sleep(.5)
        try:
            if os.path.isfile(plotfilepath):
                filethere = 0
        except FileNotFoundError:
            continue

    with open(plotfilepath) as tfile:
        pfile_contents = tfile.read()
    return render_template_string(pfile_contents)


#if __name__ == '__main__':
    #serve(app)

    #app.run('127.0.0.1', 5000, debug=True)  (nginx?)

