

import os
from time import sleep
from flask import Flask, request, render_template, jsonify
from jinja2 import Environment, select_autoescape
import appsupport
from flask_cors import CORS, cross_origin
import os

application = Flask(__name__)
CORS(application, resources={r"/*": {"origins": "*"}})

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


@application.route('/abc')
def index():
    return render_template('index.html')  ## has the user entry form


@cross_origin()
@application.route('/getpy', methods=["GET", "POST", "UPDATE", "HEAD"])
def getpy():
    # if request.method == 'POST':
    #     print('Incoming POST')

    # GET request
    if request.method == 'GET':
        # message = {'greeting': 'Hello from Flask!'}
        print("Incoming GET")

    formdata = request.values.dicts[0]

    formdict = {"initial_supply_y": formdata.get('initsup'),
                "annual_inflation": formdata.get('anninf'),
                "start_inflation": formdata.get('startinf'),
                "stop_inflation_y": formdata.get('stopinf'),
                "disinflation_ratio": formdata.get('disinf'),
                "timestp": formdata.get('timestp')}

    args_dict = make_names(formdict)
    tk_obj = appsupport.AppSupport()

    tk_obj.main(args_dict)

    # chk_file = chk_for_file(args_dict.get('plotfilepath'))
    print("got this far! file should be there")
    return '200 OK'


def make_names(args_dict):
    if os.name == 'nt':
        app_root = "E:/wsvue/vuetify-material-dashboard-master/src/assets"
        # app_root = os.path.abspath(os.curdir)
    else:
        # app_root = '/home/jetgal/psucalc'  # pythonanywhere
        app_root = '/usr/share/nginx/html/tokenlife'

    plotsdir = 'plots'
    plotfilesdir = os.path.join(app_root, plotsdir)
    timestp = args_dict.get("timestp")
    args_dict.update({"timestp": timestp})

    # main real plot is time or _t
    plot_name_t = "plot" + timestp + ".svg"
    plot_name_w = "plotwatch.svg"
    plot_name_r = "plotreal.svg"  # same as "two", not as permanent as timed

    plotfp_t = os.path.join(plotfilesdir, plot_name_t)
    plotfp_w = os.path.join(plotfilesdir, plot_name_w)
    plotfp_r = os.path.join(plotfilesdir, plot_name_r)

    plotfilepath_t = os.path.normpath(plotfp_t)
    plotfilepath_w = os.path.normpath(plotfp_w)
    plotfilepath_r = os.path.normpath(plotfp_r)

    args_dict.update({"plotfilepath_t": plotfilepath_t})
    args_dict.update({"plot_name_t": plotfp_t})  # time stamped for later

    args_dict.update({"plotfilepath_w": plotfilepath_w})
    args_dict.update({"plot_name_w": plotfp_w})  # w = watched

    args_dict.update({"plot_name_r": plot_name_r})  # real or two
    args_dict.update({"plotfilepath_r": plotfilepath_r})

    return args_dict


if __name__ == "__main__":
    application.run(debug=1, host='localhost', port=5002)




    # serve(app, listen='0.0.0.0:8082')
    # serve(app, unix_socket='/tmp/tokenlife.sock')
#https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04


    # args_dict = {"initial_supply_y": initial_supply_y,
    #              "stop_inflation_y": stop_inflation_y,
    #              "disinflation_ratio": disinflation_ratio,
    #              "annual_inflation": annual_inflation,
    #              "start_inflation": start_inflation,
    #              "timestp": timestp,
    #              "plotfilepath": plotfilepath,
    #              "plotsvg": plot_name}

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
