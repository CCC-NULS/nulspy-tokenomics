#

from waitress import serve
from time import sleep
from os import path
from flask import Flask, request, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
from datetime import datetime
from ./token
from app_support_code import nocache
from app_support_code import AppSupport as ac
#sys.stderr = sys.stdout   rootloglev = 40

app = Flask(__name__)

env = Environment(    # jinja2
    loader=PackageLoader('psu-calc', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
)
#-----------------------------------------------------------------------------
def main_work(site, just_name):   # run LinkCheck and ac.myprint to console
    ac.myprint("running main_work. site is: " + site)
    os_path_plus_stat = path.join(app.root_path, "static")
    file_path = path.join(os_path_plus_stat, just_name)

    lc = TokenLife()
    answers, redirs = lc.main(site)
    len_ans = len(answers)
    len_red = len(redirs)
    if len_ans + len_red == 0:
        ac.write_html_file(file_path, [('', '', '')], [('', '', '')], special=1)  #special=1 is a page with no broken links
    else:
        ac.write_html_file(file_path, answers, redirs)
    dt = str(datetime.now())
    print( dt + "  main_work done")

    #-----------------------------------------------------------------------------


@app.route('/')
def index():
    return render_template('index.html')  ## has a form

@nocache             # very important so client server doesn'w_thread cache results
@app.route('/indexn', methods = ['POST', 'GET', 'HEAD'])
def indexn():  # git name of url, construct names and pages, present page with button to next step

    name = request.form['name']  # from index.html   # the site
    print("----------------------------------------------------")
    print("Starting over. site is: ", name)
    sleep(2)
    return render_template('indexn.html', name = name)  ## has a form

@nocache             # very important so client server doesn'w_thread cache results
@app.route('/indexnn', methods = ['POST', 'GET', 'HEAD'])
def indexnn():  # git name of ur
    name = request.form['name']  # from index.html  the site name
    timestp1 = format(datetime.now(), '%Y%m%d%H%M%S')
    just_name = "res" + timestp1 + ".html"
    just_name_st = "./static/" + just_name

    print("just made names just_name and just_name_st: " + just_name + "  " + just_name_st)
    main_work(name, just_name)
    sleep(3)
    return render_template('indexnn.html', filename=just_name_st)  ## has a form


if __name__ == '__main__':
    serve(app)
    #app.run('127.0.0.1', 5000, debug=True)
