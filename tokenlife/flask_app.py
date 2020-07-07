
from flask import Flask, request, render_template, jsonify
from jinja2 import Environment, select_autoescape
import appsupport
from flask_cors import CORS, cross_origin
import os

application = Flask(__name__)
CORS(application, resources={r"/*": {"origins": "*"}})

env = Environment(
    autoescape=select_autoescape(['html', 'xml']),
)

@application.route('/static')
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
        print("Incoming GET")

    formdata = request.values.dicts[0]
    if len(formdata) > 2:
        if os.name == 'nt':
            basedir = "E:/wsvue/tokenlifevue/pythonmod/static"
        else:  # linux
            basedir = "/usr/share/nginx/html/tokenlife/plots"

        formdict = {"initial_supply_y": formdata.get('initsup'),
                    "annual_inflation": formdata.get('anninf'),
                    "start_inflation": formdata.get('startinf'),
                    "stop_inflation_y": formdata.get('stopinf'),
                    "disinflation_ratio": formdata.get('disinf'),
                    "timestp": formdata.get('timestp'),
                    "basedir": basedir}
        args_dict = make_names(formdict)
        tk_obj = appsupport.AppSupport()  # make obj
        tk_obj.main(args_dict)    # execute main
        print("got this far! file should be there. ")
        return '200 OK'


def make_names(args_dict):
    timestamp = args_dict.get("timestp")
    basedir = args_dict.get("basedir")
    plot_name_time_stmp = "plot" + timestamp + ".svg"  # the rest are saved as jpgs with timestamps
    plotpath_timestp = os.path.join(basedir, plot_name_time_stmp)  # t for timestamp - names have timestamp
    plotpath_timestp_norm = os.path.normpath(plotpath_timestp)
    args_dict.update({"plotpath_timestp": plotpath_timestp_norm})  # time stamped for later, jpg
    return args_dict


if __name__ == "__main__":
    application.run(debug=1, host='0.0.0.0', port=8084)

