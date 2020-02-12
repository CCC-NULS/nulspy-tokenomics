# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:53:45 2020
@author: Kathy Norman and Nancy Schorr
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from math import ceil


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
        self.inflation_intervals = None
        self.interval_limit_x = None
        self.ones_list = []
        self.the_div = None

    def checkthis(self, bignum):
        a = len(str(int(bignum)))
        b = a - 3
        c = 10**b
        return c

    def main(self, args_dict):
        the_div = self.checkthis(args_dict.get("initial_supply_y"))
        self.the_div = the_div
        self.initial_supply_y = int(args_dict.get("initial_supply_y"))/the_div  # 100,000,000  NULS
        self.stop_inflation_y = int(args_dict.get("stop_inflation_y"))/the_div   # 210,000,000  NULS
        self.disinflation_ratio = float(args_dict.get("disinflation_ratio"))
        self.annual_inflation = int(args_dict.get("annual_inflation"))/the_div  # 5,000,000 NULS
        self.inflation_intervals = int(args_dict.get("inflation_intervals"))
        self.interval_inflation_rate = self.annual_inflation / 12  # 5,000,000 NULS
        plotfilepath = args_dict.get("plotfilepath")

        tokens = self.initial_supply_y
        self.interval_limit_x = 75 * 12
        self.interval_count_list_x = [i for i in range(1, self.interval_limit_x)]

        for i in self.interval_count_list_x:
            if tokens >= self.stop_inflation_y:
                self.interval_inflation_rate = self.interval_inflation_rate * (1 - self.disinflation_ratio)
            tokens = tokens + self.interval_inflation_rate
            self.token_count_list_y.append(int(tokens))
            self.ones_list.append(1)
        self.plot_graph(plotfilepath)
        return True

    def roundup(self, nm):
        num = int(nm)
        amt = len(str(num))-1
        multiplier = 10 ** amt
        newval = ceil(num/multiplier)*multiplier
        return newval

    def plot_graph(self, plotfilepath):
        plt.ioff()
        font = {'size': 12}
        disinflation_ratio = self.disinflation_ratio

        interval_inflation = str(round(self.annual_inflation * self.the_div / 12))
        bottom_x = 0
        top_x = int(self.interval_limit_x + (self.interval_limit_x / 10))
        bottom_y = self.initial_supply_y
        top_y = int(self.token_count_list_y[-1])

        disinflation = "{:.1%}".format(disinflation_ratio)
        matplotlib.rc('font', **font)
        fig, ax = plt.subplots(figsize=(12, 9))

# -------- TICKS
        top_x = int(self.roundup(top_x))  # round up

        min_x_gaps = int(top_x / 20)
        major_x_gaps = int(top_x / 10)

        min_y_gaps = int(top_y / 20)
        major_y_gaps = int(top_y / 10)

        major_ticks_x = np.arange(bottom_x, top_x, major_x_gaps)
        minor_ticks_x = np.arange(bottom_x, top_x, min_x_gaps)

        major_ticks_y = np.arange(bottom_y, top_y,  major_y_gaps)
        bottom_y_start = bottom_y + min_y_gaps

        minor_ticks_y = np.arange(bottom_y_start, top_y, min_y_gaps)

        ax.set_xlim(xmin=0, xmax=top_x)
        ax.set_ylim(ymin=bottom_y, ymax=top_y)
        ax.set_yticks(major_ticks_y)
        ax.set_yticks(minor_ticks_y, minor=True)

        ax.set_xticks(major_ticks_x)
        ax.set_xticks(minor_ticks_x, minor=True)
        ax.ticklabel_format(style='plain')

        ax.grid(which='both')

        plt.title('Life Span for Token', pad=20, color="purple", size=30)
        isstr = 'Initial Supply: {}'.format(str(bottom_y))
        xlabel_str = "30 day intervals " + interval_inflation + " inflation and " + disinflation + " deflation"

        ylabel_str = 'Tokens in increments of 100 M'

        plt.ylabel(ylabel_str, size=20, color="green", labelpad=2)
        plt.xlabel(xlabel_str, size=20, labelpad=20, color="blue")
       
        plt.suptitle("Lifespan for Token " + self.TOKEN_SYMBOL, size=16, y=4, color="red")

        plt.plot(self.token_count_list_y, color='purple', linestyle='-', linewidth=2)

        plt.legend([isstr, 'Token Initial Supply'], loc='lower left')
        plt.savefig(plotfilepath,  dpi=150, format='svg')
        #plt.show()
        return True
