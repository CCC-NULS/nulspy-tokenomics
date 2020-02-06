# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:53:45 2020
@author: Kathy Norman and Nancy Schorr
"""

import matplotlib.pyplot as plt
from datetime import datetime
from requests import post

class app_support:
    def __init__(self):
        self.TOKEN_SYMBOL = "VKG"  # 3 characters, all caps.  e.g SET = Space Exploration
        self.initial_supply = 100000000  # 100,000,000  NULS
        self.stop_inflation = 210000000  # 210,000,000  NULS
        self.deflation_ratio = 0.004
        self.annual_inflation = 5000000  # 5,000,000 NULS
        self.intervals_till_start_infl = 24
        self.interval_inflation_rate = self.annual_inflation / 12  # 5,000,000 NULS

        self.token_count_list = []
        self.interval_count_list = []

    # args_dict = { "ini_sup": initial_supply,    "stop_i": stop_inflation,     "defl": deflation_ratio,
    # "ann_inf": annual_inflation,             "inf_interval":          intervals_till_start_infl}

    def main(self, args_dict) -> str:
        self.TOKEN_SYMBOL = "VKG"  # 3 characters, all caps.  e.g SET = Space Exploration

        self.initial_supply = int(args_dict.get("ini_sup"))  # 100,000,000  NULS
        self.stop_inflation = int(args_dict.get("stop_i"))   # 210,000,000  NULS
        self.deflation_ratio = float(args_dict.get("defl"))
        self.annual_inflation = int(args_dict.get("ann_inf"))  # 5,000,000 NULS
        self.intervals_till_start_infl = int(args_dict.get("inf_interval"))
        timestp = int(args_dict.get("timestp"))
        self.interval_inflation_rate = self.annual_inflation / 12  # 5,000,000 NULS

        tokens = self.initial_supply
        print("\n ----- ----- ----->   Starting token count: ", tokens)
        print("self.start_inflation: ", self.intervals_till_start_infl)

        interval_limit = 75 * 12
        print("  Interval limit: ", interval_limit)
        self.interval_count_list = [i for i in range(1, interval_limit)]
        print(" interval_inflation_rate: ", self.interval_inflation_rate)

        for interval_count in self.interval_count_list:
            print("\n -- Current interval_count: ", interval_count)

            if tokens >= self.stop_inflation:
                mynumber = self.interval_inflation_rate * (1 - self.deflation_ratio)
                print("\n\n mynumber: ", mynumber)
                self.interval_inflation_rate = self.interval_inflation_rate * (1 - self.deflation_ratio)
                print("now in deflation. Interval_inflation is: ", self.interval_inflation_rate)

            tokens = tokens + self.interval_inflation_rate
            print("new count of tokens: ", tokens)
            self.token_count_list.append(tokens)
            print("\n\n")
        print("and we are done with calcs")
        fname = "plots/plot" + timestp + ".svg"
        self.plot_graph(fname)

    def plot_graph(self, fname) -> str:

        plt.title('Token Life - Token Supply')
        plt.legend(['Initial Supply: ', self.initial_supply], loc='upper left')
        #
        xlabel_str = '30 day intervals'
        ylabel_str = self.TOKEN_SYMBOL + ' Token Count, increments of 1M'
        plt.ylabel(ylabel_str)
        plt.grid(True)
        plt.xlabel(xlabel_str)
        plt.xlabel("yes")
        plt.suptitle(" Life Span for token " + self.TOKEN_SYMBOL)
        plt.plot(self.interval_count_list, self.token_count_list)
        plt.savefig(fname,  dpi=150, format='svg')



    # def write_html_file(self, fname):
    #     a1 = "<html><head></head><body>"
    #     a2 = "<script>  img = document.createElement('img'); img.src = 'plots/plot-5202157.svg;"
    #     a3 = "document.getElementById('body').appendChild(img);   </script>"
    #     a4 = "</body></html>"
    #     a5 = a1 + a2 + a3 + a4
    #     f = open(fname, 'w')
    #     f.write(a5)
    #     f.close()
