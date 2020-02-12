# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:53:45 2020
@author: Kathy Norman and Nancy Schorr
"""
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib
from matplotlib import axes
import sys
import numpy as np


class AppSupport:
    def __init__(self):
        self.TOKEN_SYMBOL = "VKG"  # 3 characters, all caps.  e.g SET = Space Exploration
        self.initial_supply_y = 0
        self.stop_inflation_y = 0
        self.disinflation_ratio = 0
        self.annual_inflation = 0
        self.intervals_till_start_infl = 0
        self.interval_inflation_rate_list = self.annual_inflation / 12  # 5,000,000 NULS
        self.token_count_list_y = []
        self.interval_count_list_x = []
        self.interval_supply_list = [i for i in range(1, 900)]
        self.interval_inflation_rate = None
        self.interval_limit_x = None
        self.ones_list = []

    def main(self, args_dict):
        self.initial_supply_y = int(args_dict.get("initial_supply_y"))  # 100,000,000  NULS
        self.stop_inflation_y = int(args_dict.get("stop_inflation_y"))   # 210,000,000  NULS
        self.disinflation_ratio = float(args_dict.get("disinflation_ratio"))
        self.annual_inflation = int(args_dict.get("annual_inflation"))  # 5,000,000 NULS
        self.inflation_intervals = int(args_dict.get("inflation_intervals"))
        self.interval_inflation_rate = self.annual_inflation / 12  # 5,000,000 NULS
        plotfilepath = args_dict.get("plotfilepath")
        #print("nms - {}  ".format(plotfilepath), file=sys.stderr)

        tokens = self.initial_supply_y
        # print("\n ----- ----- ----->   Starting token count: ", tokens)  print("self.start_inflation: ",
        # self.intervals_till_start_infl)

        self.interval_limit_x = 75 * 12                         # print("  Interval limit: ", interval_limit_x)
        self.interval_count_list_x = [i for i in range(1, self.interval_limit_x)]    # print(" interval_inflation_rate: ",
                                                            # self.interval_inflation_rate)

        for i in self.interval_count_list_x:  # print("\n -- Current interval_count: ", interval_count)

            if tokens >= self.stop_inflation_y:
                self.interval_inflation_rate = self.interval_inflation_rate * (1 - self.disinflation_ratio)
                    # mynumber = self.interval_inflation_rate * (1 - self.disinflation_ratio)
                    # print("\n\n mynumber: ", mynumber)
                    # print("now in deflation. Interval_inflation is: ", self.interval_inflation_rate)

            tokens = tokens + self.interval_inflation_rate      # print("new count of tokens: ", tokens)
            self.token_count_list_y.append(tokens)               # print("and we are done with calcs")
            self.ones_list.append(1)
        self.plot_graph(plotfilepath)
        return True

    def plot_graph(self, plotfilepath):
        #print("!!! nms ---------------- plotfilepath: {}".format(plotfilepath), file=sys.stderr)
        font = {'size': 12}
        disinflation_ratio = self.disinflation_ratio
        inflation = str(self.annual_inflation)
        BOTTOM_X = 0
        TOP_X = self.interval_limit_x + (self.interval_limit_x /10)
        BOTTOM_Y = self.initial_supply_y
        TOP_Y = self.token_count_list_y[-1]

        disinflation = "{:.1%}".format(disinflation_ratio)
        matplotlib.rc('font', **font)
# ---------------------------------------------- plt
        fig, ax = plt.subplots(figsize=(12, 9))
        int_plus = TOP_X * .1    # add 10% to x axis
        x_last = TOP_X + int_plus                                           #  interlist[-1]
        # interlist_x = [i for i in range(0, x_last, 50)]

        print("token_count_list_y ", TOP_Y)

# -------- TICKS
        min_x_plugs = TOP_X / 20
        major_x_plugs = TOP_X / 10

        min_y_plugs = TOP_Y / 20
        major_y_plugs = TOP_Y / 10

        major_ticks_x = np.arange(BOTTOM_X, TOP_X, major_x_plugs)
        minor_ticks_x = np.arange(BOTTOM_X, TOP_X, min_x_plugs)

        major_ticks_y = np.arange(BOTTOM_Y, TOP_Y,  major_y_plugs)
        BOTTOM_Y_start = BOTTOM_Y + min_y_plugs
        minor_ticks_y = np.arange(BOTTOM_Y_start, TOP_Y, min_y_plugs)

        ax.set_xlim(xmin=BOTTOM_X, xmax=TOP_X)
        ax.set_ylim(ymin=BOTTOM_Y, ymax=TOP_Y)
        ax.set_yticks(major_ticks_y)
        ax.set_yticks(minor_ticks_y, minor=True)

        ax.set_xticks(major_ticks_x)
        ax.set_xticks(minor_ticks_x, minor=True)

        ax.grid(which='both')

        plt.title('Token Life - Token Supply', pad=20, color="purple", size=30)
        isstr = 'Initial Supply: {}'.format(str(BOTTOM_Y))

        xlabel_str = "30 day intervals - {} inflation and {} deflation".format(inflation, disinflation)
        ylabel_str = self.TOKEN_SYMBOL + ' Tokens in increments of 100 M'

        plt.ylabel(ylabel_str, size=20, color="green", labelpad=2)
        plt.xlabel(xlabel_str, size=20, labelpad=20, color="blue")
       
        plt.suptitle("Lifespan for Token " + self.TOKEN_SYMBOL, size=16, y=4, color="red")

        plt.plot(self.token_count_list_y, color='purple', linestyle='-', linewidth=2)

        plt.legend([isstr, 'Token Initial Supply'], loc='lower left')
        plt.savefig(plotfilepath,  dpi=150, format='svg')
        plt.show()
        return True
