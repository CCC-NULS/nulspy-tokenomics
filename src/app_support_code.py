from config import conf_debug
from flask import make_response
from functools import wraps, update_wrapper
from datetime import datetime


class AppSupport:

    @staticmethod
    def myprint(print_str):
        if conf_debug:   # change in file config.py
            print(print_str)

    @classmethod
    def write_html_file(cls, filey, data, redirs, special=0):
        first = "<br><span id='errline2'> BAD LINK--> </span> "
        sec = "<br><span id='errline'>&nbsp;*** ERROR-->  "
        third = "&emsp;&emsp;---> Found on: "
        fourth = "Here are your broken links:"
        fifth = "Here are your 301 permanent redirect errors which aren't as serious -- but should be fixed:"
        if special == 1:
            first = "No broken links."
            sec = "No errors found."
            third = ""
            fourth = "Thanks for using LinkCheck."

        f = open(filey, 'w')
        f.write("<p></p><h3>" + fourth + "</h3>")

        for line in data:
            f.write(first)
            f.write("<a href='" + str(line[0]) + "'>")
            f.write(str(line[0])+ "</a>&ensp;")
            f.write(sec + str(line[1])+ "</span>&ensp;")  ## the error  # span needed!!
            f.write("<br>&ensp;&ensp;" + third + "<a href='")
            f.write(str(line[2]) + "' >")
            f.write(str(line[2])+ "</a><br>")

        f.write('<p>&nbsp;</p><h3 style="font-size:12px;font-weight:500;" >' + fifth + "</h3>")

        for line in redirs:
            f.write(first)
            f.write("<a href='" + str(line[0]) + "'>")
            f.write(str(line[0])+ "</a>&ensp;")
            f.write(sec + str(line[1])+ "</span>&ensp;")  ## the error  # span needed!!
            f.write("<br>&ensp;&ensp;" + third + "<a href='")
            f.write(str(line[2]) + "' >")
            f.write(str(line[2])+ "</a><br>")

        f.close()


def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return update_wrapper(no_cache, view)