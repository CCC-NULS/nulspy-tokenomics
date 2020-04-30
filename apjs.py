#!/c/Program Files/Python37/python.exe
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:53:45 2020
@author: Kathy Norman and Nancy Schorr
"""
import os
from datetime import datetime
from math import floor
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import StrMethodFormatter


class Apjs:
    def __init__(self):
        self.TOKEN_SYMBOL = "NUL"  # 3 characters, all caps.  e.g SET = Space Exploration
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

    def main(self, argvs):
        newar = list()

        for v in range(1, 6):
            # print(argvs[v])
            narg = argvs[v]
            nint = int(narg)
            newar.append(nint)

        if os.name == 'nt':
            app_root = "E:/PycharmProjects/CCC/nulspy-tokenomics"  # E:/PycharmProjects/CCC/nulspy-tokenomics/
            # app_root = os.path.abspath(os.curdir)
        else:
            # app_root = '/home/jetgal/psucalc'  # pythonanywhere
            app_root = '/usr/share/nginx/html/tokenlife'
        timestp = format(datetime.now(), '%d%H%M%S')
        plot_name = "plot" + timestp + ".svg"
        plotsdir = 'plotfiles'
        plotfilesdir = os.path.join(app_root, plotsdir)
        plotfp = os.path.join(plotfilesdir, plot_name)
        plotfilepath = os.path.normpath(plotfp)

        self.initial_supply_y = int(newar[0])  # 100,000,000  NULS
        self.annual_inflation = int(newar[1])  # 5,000,000 NULS
        start_inflation = int(newar[2])        # 24
        self.stop_inflation_y = int(newar[3])   # 210,000,000  NULS
        disratio = int(newar[4])  # 0.004
        self.disinflation_ratio = float(disratio / 1000)  # 0.004
        self.real_initial_supply_y = int(newar[0])

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
            # print(tokens, monthly_inflation, deflation, interval_count)
            interval_count += 1

        self.plot_graph(plotfilepath)

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

    def plot_graph(self, plotfilepath):
        plt.ioff()
        font = {'size': 12}
        disinflation_ratio = self.disinflation_ratio
        bottom_x = 0
        top_x = int(self.interval_limit_x)

        bottom_y = self.initial_supply_y

        top_count = self.token_count_list_y[-1]
        top_y = int(top_count)

        if self.stop_inflation_y > top_y:
            top_y = self.stop_inflation_y

        disinflation = "{:.1%}".format(disinflation_ratio)
        matplotlib.rc('font', **font)

        fig, ax = plt.subplots(figsize=(14, 9))

        stp_inf = self.stop_inflation_y
        vpadding = top_y / 22
        plt.axhline(y=stp_inf, xmin=0, xmax=top_x, linewidth=2, linestyle='-.', color='r')
        text_loc = self.stop_inflation_y + (vpadding/5)

        plt.text(100, text_loc, 'Max Supply', color='r', size='large', weight='bold')
        ylocation = self.initial_supply_y + vpadding
        plt.text(100, ylocation, '-----  Token Growth Over Time', color='purple', size='x-large',
                 weight='bold')

        plt.margins(y=1.2, tight=False)

        plt.figtext(0.01, 0, 'Hit Back Button to Start Over',  color='b',  size='medium')

        # -------- TICKS

        gx = int(top_x / 10)
        major_x_gaps = self.round_up_to_multiple(gx, 100)
        major_ticks_x = np.arange(bottom_x, top_x, major_x_gaps)

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

        plt.title('Life Span for Token', pad=20, color="purple", size=30)

        an_infl = str("{:,}".format(round(self.annual_inflation / 12)))
        part2 = " Inflation, and Disinflation Ratio: "
        xlabel_str = "30 day Intervals, " + an_infl + part2 + disinflation
        ylabel_str = 'Total Supply'

        plt.ylabel(ylabel_str, size=18, color="green", labelpad=7)
        plt.xlabel(xlabel_str, size=18, labelpad=20, color="blue", weight="bold")

        plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))  # No decimal places

        plt.suptitle("Lifespan for Token " + self.TOKEN_SYMBOL, size=16, y=4, color="red")

        plt.plot(self.token_count_list_y, color='purple', linestyle='-', linewidth=3)

        plt.savefig(plotfilepath,  dpi=150, format='svg')
        return True


if __name__ == "__main__":
    import sys
    ap = Apjs()
    # for i in sys.argv:
    #     print(i)
    # mylist = ['100000000', '5000000', '24', '210000000', '0.004']
    ap.main(sys.argv)
    # python ./apjs.py 100000000 5000000 24 210000000 0.004
    # args="100000000 5000000 24 210000000 4"