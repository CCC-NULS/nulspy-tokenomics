

import os
from datetime import datetime
from time import sleep
from flask import Flask, request, render_template, render_template_string
from jinja2 import Environment, select_autoescape
import appsupport


application = Flask(__name__)

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


@application.route('/')   # change later
def index():
    return render_template('index.html')  ## has the user entry form


@application.route('/post', methods=["GET"])   # change later
def show_post():
    initial_supply_y = request.args.get('a')
    annual_inflation = request.args.get('b')
    start_inflation = request.args.get('c')
    stop_inflation_y = request.args.get('d')
    disinflation_ratio = request.args.get('e')

    if os.name == 'nt':
        app_root = "E:/PycharmProjects/CCC/nulspy-tokenomics"
        # app_root = os.path.abspath(os.curdir)
    else:
        # app_root = '/home/jetgal/psucalc'  # pythonanywhere
        app_root = '/usr/share/nginx/html/tokenlife'

    timestp = format(datetime.now(), '%d%H%M%S')
    plot_name = "plot" + timestp + ".svg"
    plotsdir = 'plotfiles'
    plotfilesdir = os.path.join(app_root, plotsdir)
    plotfp = os.path.join(plotfilesdir, plot_name)
    plotfilepath = os.path.normpath(plotfp)

    args_dict = {"initial_supply_y": initial_supply_y,
                 "stop_inflation_y": stop_inflation_y,
                 "disinflation_ratio": disinflation_ratio,
                 "annual_inflation": annual_inflation,
                 "start_inflation": start_inflation,
                 "timestp": timestp,
                 "plotfilepath": plotfilepath,
                 "plotsvg": plot_name}

    tk_obj = appsupport.AppSupport()
    tk_obj.main(args_dict)

    chk_for_file(plotfilepath)

    with open(plotfilepath) as tfile:
        pfile_contents = tfile.read()
    return render_template_string(pfile_contents)

# @application.route('/plotfiles', methods=['GET', 'POST', 'HEAD'])
# def plots():
#     # os.chdir("..")
#     if os.name == 'nt':
#         app_root = "E:/PycharmProjects/psu-calc"
#         # app_root = os.path.abspath(os.curdir)
#     else:
#         # app_root = '/home/jetgal/psucalc'  # pythonanywhere
#         app_root = '/usr/share/nginx/html/tokenlife'
#
#     timestp = format(datetime.now(), '%d%H%M%S')
#     plot_name = "plot" + timestp + ".svg"
#     plotsdir = 'plotfiles'
#     plotfilesdir = os.path.join(app_root, plotsdir)
#     plotfp = os.path.join(plotfilesdir, plot_name)
#     plotfilepath = os.path.normpath(plotfp)
#
#     initial_supply_y = request.form['initial_supply_y']  # from index.html   # the site
#     annual_inflation = request.form['annual_inflation']  # from index.html   # the site
#     start_inflation = request.form['start_inflation']  # from same place
#     stop_inflation_y = request.form['stop_inflation_y']  # from index.html   # the site
#     disinflation_ratio = request.form['disinflation_ratio']  # from index.html   # the site
#
#     args_dict = {"initial_supply_y": initial_supply_y,
#                  "stop_inflation_y": stop_inflation_y,
#                  "disinflation_ratio": disinflation_ratio,
#                  "annual_inflation": annual_inflation,
#                  "start_inflation": start_inflation,
#                  "timestp": timestp,
#                  "plotfilepath": plotfilepath,
#                  "plotsvg": plot_name}
#
#     tk_obj = appsupport.AppSupport()
#     tk_obj.main(args_dict)
#
#     chk_for_file(plotfilepath)
#
#     with open(plotfilepath) as tfile:
#         pfile_contents = tfile.read()
#     return render_template_string(pfile_contents)


if __name__ == "__main__":
    application.run(host='0.0.0.0')




    # serve(app, listen='0.0.0.0:8082')
    # serve(app, unix_socket='/tmp/tokenlife.sock')
#https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04


