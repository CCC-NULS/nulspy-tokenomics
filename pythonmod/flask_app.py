

from time import sleep
from flask import Flask, request, render_template, jsonify
from jinja2 import Environment, select_autoescape
import appsupport
from flask_cors import CORS, cross_origin
import os
from shutil import copyfile

application = Flask(__name__)
CORS(application, resources={r"/*": {"origins": "*"}})

env = Environment(    # jinja2
    autoescape=select_autoescape(['html', 'xml']),
)


def chk_for_file(tfile):
    sleep(.4)
    while True:
        try:
            x = os.path.isfile(tfile)
            if x:
                return True
            else:
                sleep(.3)
        except FileNotFoundError:
            continue


@application.route('/abc')
def index():
    return render_template('index.html')  ## has the user entry form


@cross_origin()
@application.route('/getpy', methods=["GET", "POST", "UPDATE", "HEAD"])
def getpy():
    basedir = None
    if request.method == 'POST':
        print('Incoming POST')

    # GET request
    if request.method == 'GET':
        # message = {'greeting': 'Hello from Flask!'}
        print("Incoming GET")

    formdata = request.values.dicts[0]
    if len(formdata) > 2:
        if os.name == 'nt':
            basedir = "E:/wsvue/tokenlifevue/src/assets/plots/"
        else:  # linux
            basedir = "/usr/share/nginx/html/tokenlifevue/src/assets/plots/"

        formdict = {"initial_supply_y": formdata.get('initsup'),
                    "annual_inflation": formdata.get('anninf'),
                    "start_inflation": formdata.get('startinf'),
                    "stop_inflation_y": formdata.get('stopinf'),
                    "disinflation_ratio": formdata.get('disinf'),
                    "timestp": formdata.get('tdate'),
                    "basedir": basedir}

        args_dict = make_names(formdict)
        tk_obj = appsupport.AppSupport()  # make obj
        tk_obj.main(args_dict)    # execute main
        print("got this far! file should be there. ")
        timefilepth = make_temp_file(basedir, args_dict.get('timestp'))
        file_there = chk_for_file(timefilepth)
        print("got this far! file should be there: " + str(file_there))
        return '200 OK'


def chk_for_file(tfile):
    sleep(.4)
    while True:
        try:
            x = os.path.isfile(tfile)
            if x:
                return True
            else:
                sleep(.3)
        except FileNotFoundError:
            continue

def make_temp_file(timedir, timest):         #  make temp file as placeholder
    # esquare = basedir + "bluecube.svg"  # empty square placeholder
    # pltreal = basedir + "pltreal.svg"
    # copyfile(esquare, pltreal)
    print("inside make_temp_file")

    plotnonepath = timedir + "plotnone.vue"  # empty component
    timefilepath = timedir + "plot" + timest + ".vue"
    copyfile(plotnonepath, timefilepath)
    print("plotnone: " + plotnonepath)
    print("timefilepath: " + timefilepath)
    return timefilepath


def make_names(args_dict):
    timestamp = args_dict.get("timestp")
    basedir = args_dict.get("basedir")

    # plot_name_generic = "pltreal.svg"
    plot_name_time_stmp = "plot" + timestamp + ".svg"  # the rest are saved as jpgs with timestamps
    file_time_stmp = "temp" + timestamp + ".txt"  # the rest are saved as jpgs with timestamps

    # plotpath_generic = os.path.join(basedir, plot_name_generic)  # put real one in components so router can update
    plotpath_timestp = os.path.join(basedir, plot_name_time_stmp)  # t for timestamp - names have timestamp
    plotpath_tfile = os.path.join(basedir, file_time_stmp)  # t for timestamp - names have timestamp

    plotpath_timestp_norm = os.path.normpath(plotpath_timestp)
    # plotpath_generic_norm = os.path.normpath(plotpath_generic)
    plotpath_tfile_norm = os.path.normpath(plotpath_tfile)

    args_dict.update({"plotpath_timestp": plotpath_timestp_norm})  # time stamped for later, jpg
    # args_dict.update({"plotpath_generic": plotpath_generic_norm})  # generic name, svg
    args_dict.update({"plotpath_tfile": plotpath_tfile_norm})  # generic name, svg
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
