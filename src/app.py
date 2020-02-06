#
# from time import sleep

from waitress import serve
from flask import Flask, request, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
import app_support_code

app = Flask(__name__)
env = Environment(    # jinja2
    # loader=PackageLoader('psu-calc', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),

)


@app.route('/')   # change later
def index():
    return render_template('index.html')  ## has the user entry form


@app.route('/show',  methods=['POST', 'GET', 'HEAD'])
def show():
    initial_supply = request.form['initial_supply']  # from index.html   # the site
    stop_inflation = request.form['stop_inflation']  # from index.html   # the site
    deflation_ratio = request.form['deflation_ratio']  # from index.html   # the site
    annual_inflation = request.form['annual_inflation']  # from index.html   # the site
    inflation_intervals = request.form['start_inflation']  # from same place

    print("got these", initial_supply, stop_inflation, deflation_ratio, annual_inflation,
          inflation_intervals  )
    interval_inflation_tokens = annual_inflation / 12  # 5,000,000 NULS
    # start_inflation = 2 * 12  # add later as entry
    #start_inflation
    #return render_template('show.html', name="Hello Joe")  ## has a form

#
#
#
#
# @app.route('/')
# def index():
#     return render_template('../templates/index.html')  ## has a form
#
#
# @app.route('/indexn', methods=['POST', 'GET', 'HEAD'])
# def indexn():  # git name of url, construct names and pages, present page with button to next step
#     name = request.form['name']  # from index.html   # the site
#
#     initial_supply = request.form['initial_supply']  # from index.html   # the site
#     stop_inflation = request.form['stop_inflation']  # from index.html   # the site
#     deflation_ratio = request.form['deflation_ratio']  # from index.html   # the site
#     annual_inflation = request.form['annual_inflation']  # from index.html   # the site
#     interval_inflation_tokens = annual_inflation / 12  # 5,000,000 NULS
#     start_inflation = 2 * 12
#
#     print("got these", initial_supply, stop_inflation, deflation_ratio, annual_inflation,
#           interval_inflation_tokens, start_inflation)
#
#     return render_template('indexn.html', name=initial_supply)  ## has a form



if __name__ == '__main__':
    serve(app)




    #app.run('127.0.0.1', 5000, debug=True)

#>>> from jinja2 import Template
# >>> template = Template('Hello {{ name }}!')
# >>> template.render(name='John Doe')
# u'Hello John Doe!'