

from time import sleep
from flask import Flask, request, render_template, jsonify
from jinja2 import Environment, select_autoescape
import appsupport
from flask_cors import CORS, cross_origin
import os
from datetime import datetime
from shutil import copyfile
from stat import S_IWUSR

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
    # if request.method == 'POST':
    #     print('Incoming POST')

    # GET request
    if request.method == 'GET':
        # message = {'greeting': 'Hello from Flask!'}
        print("Incoming GET")

    formdata = request.values.dicts[0]
    if len(formdata) > 2:

        formdict = {"initial_supply_y": formdata.get('initsup'),
                    "annual_inflation": formdata.get('anninf'),
                    "start_inflation": formdata.get('startinf'),
                    "stop_inflation_y": formdata.get('stopinf'),
                    "disinflation_ratio": formdata.get('disinf'),
                    "timestp": formdata.get('timestp'),
                    "gdir": formdata.get('gdir')}

        args_dict = make_names(formdict)
        tk_obj = appsupport.AppSupport()

        tk_obj.main(args_dict)

        try:
            filethere = chk_for_file(args_dict.get('plotpath_generic'))
            if not filethere:
                filethere = chk_for_file(args_dict.get('plotpath_timestp'))
        except FileNotFoundError:
            print("file not there")

        print("got this far! file should be there. " + str(filethere))

        gd = args_dict.get('gdir')
        gd_path = make_dir_name(gd)
        change_temp_file(gd_path)
        print("got this far! directory - changed temp file should be changed")
        return '200 OK'

    else:     # make dir and temp files
        gdir = formdata.get('gdir')
        timey_dir_name = make_dir_name(gdir)
        make_dir(timey_dir_name)
        make_temp_file(timey_dir_name)
        print("got this far! directory and temp file should be there")
        return '200 OK'


@cross_origin()
@application.route('/', methods=["GET", "POST", "UPDATE", "HEAD"])
def gplots():
    if request.method == 'GET':
        print("Incoming GET")


def make_dir_name(ggdir):
    if os.name == 'nt':
        plot_path_uniq1 = "E:/wsvue/tokenlifevue/pythonmod/static/plots/" + ggdir + "/"   # nms:switch

        plot_path_uniq = "E:/wsvue/tokenlifevue/src/assets/plots/" + ggdir + "/"
    else:  # linux
        plot_path_uniq = "/usr/share/nginx/html/tokenlifevue/src/assets/plots/" + ggdir + "/"
    print("make_dir_name plot_path_uniq: " + plot_path_uniq)
    return plot_path_uniq


def make_dir(timey_dir):
    ckdir = os.path.isdir(timey_dir)
    print("ckdir answer: " + str(ckdir))
    if not ckdir:    #  if false
        os.mkdir(timey_dir)


def make_temp_file(timey_dir_name):
    if os.name == 'nt':
        basedir = "E:/wsvue/tokenlifevue/src/assets/plots/"
    #  make temp file as placeholder
    esquare = basedir + "/bluecube.svg"  # empty square placeholder
    pltreal = basedir + "/pltreal.svg"
    copyfile(esquare, pltreal)


def change_temp_file(timeydir):    # to cause vue to see a change
    tempvuefile = timeydir + "watchedComp.vue"
    temp_line = "<template><div>counting more changes</div></template><script>export default {name:1}</script>"
    dtt = str(datetime.now())  # make the file different each time
    f = open(tempvuefile, "w+")
    f.write(temp_line)
    f.write(dtt)
    f.close()
    os.chmod(tempvuefile, S_IWUSR)  # write to others
    print("done changing temp file")


def make_names(args_dict):
    timestamp = args_dict.get("timestp")
    gdir = args_dict.get("gdir")
    plot_path_uniq = make_dir_name(gdir)

    # jpg plot is timeed or _t
    if os.name == 'nt':
        basedir = "E:/wsvue/tokenlifevue/src/assets/plots/"
    plot_name_generic = "pltreal.svg"
    plot_name_time_stmp = "plot" + timestamp + ".svg"  # the rest are saved as jpgs with timestamps

    plotpath_generic = os.path.join(basedir, plot_name_generic)  # put real one in components so router can update
    plotpath_timestp = os.path.join(plot_path_uniq, plot_name_time_stmp)  # t for timestamp - names have timestamp

    plotpath_timestp_norm = os.path.normpath(plotpath_timestp)
    plotpath_generic_norm = os.path.normpath(plotpath_generic)

    args_dict.update({"plotpath_timestp": plotpath_timestp_norm})  # time stamped for later, jpg
    args_dict.update({"plotpath_generic": plotpath_generic_norm})  # generic name, svg

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
