#

from waitress import serve
from time import sleep
from flask import Flask, request, render_template
from jinja2 import Environment, PackageLoader, select_autoescape


app = Flask(__name__)
env = Environment(    # jinja2
    loader=PackageLoader('psu-calc', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
)


@app.route('/index', methods=['POST', 'GET', 'HEAD'])
def index():  # git name of url, construct names and pages, present page with button to next step

    initial_supply = request.form['initial_supply']  # from index.html   # the site
    stop_inflation = request.form['stop_inflation']  # from index.html   # the site
    deflation_ratio = request.form['deflation_ratio']  # from index.html   # the site
    annual_inflation = request.form['annual_inflation']  # from index.html   # the site
    interval_inflation_tokens = annual_inflation / 12  # 5,000,000 NULS
    start_inflation = 2 * 12

    return render_template('indexn.html', name=name)  ## has a form


if __name__ == '__main__':
    serve(app)
    #app.run('127.0.0.1', 5000, debug=True)
