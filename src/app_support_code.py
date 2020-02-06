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

