
from flask import Flask, request, render_template, render_template_string
from jinja2 import Environment, select_autoescape
import appsupport
from datetime import datetime
from waitress import serve
import os
from time import sleep

app = Flask(__name__)

env = Environment(    # jinja2

    autoescape=select_autoescape(['html', 'xml']),
)


def chk_for_file(tfile):
    sleep(1.5)
    while True:
        try:
            x = os.path.isfile(tfile)
            if x:
                return True
            else:
                sleep(1)
        except FileNotFoundError:
            continue


@app.route('/')   # change later
def index():
    return render_template('index.html')  ## has the user entry form


@app.route('/plots', methods=['GET', 'POST', 'HEAD'])
def plots():
    os.chdir("..")
    base_linux = '/home/jetgal/psucalc'
    if os.name == 'nt':
        basename = os.path.abspath(os.curdir)
    else:
        basename = base_linux

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
    start_inflation = request.form['start_inflation']  # from same place

    args_dict = {"initial_supply_y": initial_supply_y,
                 "stop_inflation_y": stop_inflation_y,
                 "disinflation_ratio": disinflation_ratio,
                 "annual_inflation": annual_inflation,
                 "start_inflation": start_inflation,
                 "timestp": timestp,
                 "plotfilepath": plotfilepath,
                 "plotsvg": plotsvg}

    tk_obj = appsupport.AppSupport()
    tk_obj.main(args_dict)

    chk_for_file(plotfilepath)

    with open(plotfilepath) as tfile:
        pfile_contents = tfile.read()
    return render_template_string(pfile_contents)


if __name__ == '__main__':
    if os.name == 'nt':
        serve(app)


    #app.run('127.0.0.1', 5000, debug=True)  (nginx)

