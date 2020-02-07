
from flask import Flask, request, render_template,  escape, url_for
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
    homedir = flask.request.host_url

    template_name = "plots.html"

    timestp = format(datetime.now(), '%d%H%M%S')
    plotsvg = "plot" + timestp + ".svg"
    plotfilepath = homedir + "/plots/" + plotsvg
    p = "{0}/plots/{1}".format(homedir, plotsvg)
    print("!!!!!!!!!!!  filepath:  ", str(plotfilepath))
    imgtag = '<img src="' + plotfilepath + '" alt="Plots">'

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
                 "plotsvg": plotsvg,
                 "template_name": template_name}

    tk_obj = appsupport.AppSupport()
    tk_obj.main(args_dict)
    return render_template(template_name, data=imgtag)


if __name__ == '__main__':

    serve(app)
    a = 1


    #app.run('127.0.0.1', 5000, debug=True)  (nginx?)
