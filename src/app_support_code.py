from config import conf_debug
from flask import make_response
from functools import wraps, update_wrapper
from datetime import datetime
import app_support

class AppSupport:

    def write_html_file():
        f = open("plottemp.html", 'w')
        a1 = "<html><head></head><body>"
        a2 = "<script>  img = document.createElement('img'); img.src = 'plots/plot-5202157.svg;"
        a3 = "document.getElementById('body').appendChild(img);   </script>"
        a4 = "</body></html>"
        a5 = a1 + a2 + a3 + a4
        f.write(a5)
        f.close()

