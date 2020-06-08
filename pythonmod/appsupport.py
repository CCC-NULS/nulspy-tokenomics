# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:53:45 2020
@author: Kathy Norman and Nancy Schorr
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from math import floor
from matplotlib.ticker import StrMethodFormatter
from datetime import datetime
# import os
# import shutil
# import matplotlib.lines as lines
# import matplotlib.text as text


class AppSupport:
    def __init__(self):
        self.TOKEN_SYMBOL = "NULS"  # 3 characters, all caps.  e.g SET = Space Exploration
        self.initial_supply_y = 0
        self.stop_inflation_y = 0
        self.disinflation_ratio = 0
        self.annual_inflation = 0
        self.intervals_till_start_infl = 0
        self.token_count_list_y = []
        self.interval_count_list_x = []
        self.interval_limit_x = None
        self.ones_list = []
        self.real_initial_supply_y = None
        self.monthly_inflation = None
        self.initial_supply_list = []
        self.token_interval_list = []

    def main(self, args_dict):
        initsupply_y = args_dict.get("initial_supply_y")  # 100,000,000  NULS
        self.initial_supply_y = int(initsupply_y)  # 100,000,000  NULS
        self.stop_inflation_y = int(args_dict.get("stop_inflation_y"))   # 210,000,000  NULS
        self.disinflation_ratio = float(args_dict.get("disinflation_ratio"))/1000
        self.annual_inflation = int(args_dict.get("annual_inflation"))  # 5,000,000 NULS
        start_inflation = int(args_dict.get("start_inflation"))
        self.real_initial_supply_y = int(args_dict.get("initial_supply_y"))
        plotpath_timestp = args_dict.get("plotpath_timestp")   # jpg
        plotpath_generic = args_dict.get("plotpath_generic")   # svg

        start_inflation = start_inflation / 1000

        tokens = self.initial_supply_y
        self.interval_limit_x = 75 * 12
        monthly_inflation = self.annual_inflation / 12  # 5,000,000 NULS
        interval_count = 1

        while interval_count <= self.interval_limit_x:
            # deflation = False
            if (tokens <= self.stop_inflation_y) and (interval_count >= start_inflation):
                # deflation = True
                monthly_inflation = monthly_inflation * (1 - self.disinflation_ratio)
                tokens = tokens + monthly_inflation

            self.token_count_list_y.append(round(tokens))
            self.initial_supply_list.append(self.initial_supply_y)
            self.token_interval_list.append(interval_count)
            interval_count += 1
            name_list = [plotpath_generic, plotpath_timestp]
        tresult = self.plot_graph(name_list)
        return tresult

    # def make_long_stamp(self):
    #     datetime_str = str(datetime.now())
    #     print(datetime_str)
    #     return datetime_str

    def rounddown(self, nm):
        num = int(nm)
        amt = len(str(num))-1
        multiplier = 10 ** amt
        newval = floor(num/multiplier)*multiplier
        return newval

    # rounding up to the nearest multiple of any positive integer:
    def round_up_to_multiple(self, mynumber, multiple):
        num = mynumber + (multiple - 1)
        answer = num - (num % multiple)
        return answer

    def plot_graph(self, fnames):
        plotpath_generic, plotpath_timed = fnames
        plt.ioff()
        font = {'size': 12}
        stp_inf = self.stop_inflation_y
        dtt = str(datetime.now())
        dt = dtt[0:-7]

        disinflation_ratio = self.disinflation_ratio
        disinflation = "{:.1%}".format(disinflation_ratio)
        initial_sup_formatted = "{:,}".format(self.initial_supply_y)
        stp_inf_formatted = "{:,}".format(self.stop_inflation_y)

        max_text = 'Max Supply = ' + str(stp_inf_formatted)
        init_str = "               Initial Supply: " + initial_sup_formatted
        stop_str = "   Stop Inflation: " + str(stp_inf_formatted)
        bigstr = init_str + stop_str

        plt.margins(x=.1, y=.001, tight=False)

        top_x = int(self.interval_limit_x)
        bottom_y = self.initial_supply_y
        top_count = self.token_count_list_y[-1]
        top_y = int(top_count)
        vpadding = top_y / 22
        text_loc = self.stop_inflation_y + (vpadding/5)
        ylocation = bottom_y + vpadding

        if self.stop_inflation_y > top_y:
            top_y = self.stop_inflation_y

        matplotlib.rc('font', **font)
        fig, ax = plt.subplots(figsize=(9.6, 7.2))  # default is 6.4, 4.8 6.4, 4.8
        # fig, ax = plt.subplots(figsize=(12, 9))  default is 6.4, 4.8

        plt.subplots_adjust(left=0.17, bottom=0.19)  # controls amount of room left and below
        plt.axhline(y=stp_inf, xmin=0, xmax=top_x, linewidth=2, linestyle='-.', color='r')
        plt.text(100, text_loc, max_text, color='r', size='large', weight='bold')
        plt.text(100, ylocation, '-----  Token Growth Over Time', color='purple', size='x-large',
                 weight='bold')

        plt.figtext(0.1, 0.05, bigstr,  color='b',  size=14, weight='bold')  # bottom lines
        plt.figtext(0.007, 0.007, dt,  color='b',  size=7)   # datestamp left bottom

        # -- -- -- -- TICKS -- -- -- -- -- -- --  #

        gx = int(top_x / 10)
        major_x_gaps = self.round_up_to_multiple(gx, 100)
        major_ticks_x = np.arange(0, top_x, major_x_gaps)

        gy = int(top_y / 10)
        major_y_gaps = self.round_up_to_multiple(gy, 1000000)
        major_ticks_y = np.arange(bottom_y, top_y, major_y_gaps)

        big_x = top_x + top_x/10

        big_y = top_y + top_y/10
        ax.set_xlim(xmin=0, xmax=big_x)
        ax.set_ylim(ymin=bottom_y, ymax=big_y)

        ax.set_yticks(major_ticks_y)
        ax.set_xticks(major_ticks_x)
        ax.ticklabel_format(style='plain')

        ax.grid(which='both')

        an_infl = str("{:,}".format(round(self.annual_inflation / 12)))
        part2 = " Inflation, and Disinflation Ratio: "
        xlabel_str = "30 day Intervals, " + an_infl + part2 + disinflation
        ylabel_str = 'Total Supply'

        plt.ylabel(ylabel_str, size=14, color="green", labelpad=7)
        plt.xlabel(xlabel_str, size=16, labelpad=20, color="blue", weight="bold")

        plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))  # No decimal places

        plt.title('Life Span for Token', pad=20, color="purple", size=30)
        plt.suptitle("Lifespan for Token " + self.TOKEN_SYMBOL, size=14, y=4, color="red")

        plt.plot(self.token_count_list_y, color='purple', linestyle='-', linewidth=3)

        plt.savefig(plotpath_generic,  dpi=150, format='svg')
        plt.savefig(plotpath_timed,  dpi=150, format='png')
        #plt.show()
        return True


        # supply_label = str("{:,}".format(self.real_initial_supply_y))
        # plt.legend(['', str1], loc='lower center')
        # str1 = 'Token Growth Over Time'
        # ax.annotate('Stop Inflation Boundary', (25, text_loc))
