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


class AppSupport:
    def __init__(self):
        self.TOKEN_SYMBOL = "VKG"  # 3 characters, all caps.  e.g SET = Space Exploration
        self.initial_supply = 0
        self.stop_inflation = 0
        self.deflation_ratio = 0
        self.annual_inflation = 0
        self.intervals_till_start_infl = 0
        self.interval_inflation_rate_list = self.annual_inflation / 12  # 5,000,000 NULS
        self.token_count_list = []
        self.interval_count_list = []
        self.interval_supply_list = [i for i in range(1, 900)]
        self.interval_inflation_rate = None
        self.interval_limit = None
        self.ones_list = []

    def main(self, args_dict):
        self.initial_supply = int(args_dict.get("ini_sup"))  # 100,000,000  NULS
        self.stop_inflation = int(args_dict.get("stop_i"))   # 210,000,000  NULS
        self.deflation_ratio = float(args_dict.get("defl"))
        self.annual_inflation = int(args_dict.get("ann_inf"))  # 5,000,000 NULS
        self.intervals_till_start_infl = int(args_dict.get("inf_interval"))
        self.interval_inflation_rate = self.annual_inflation / 12  # 5,000,000 NULS
        plotfilepath = args_dict.get("plotfilepath")
        #print("nms - {}  ".format(plotfilepath), file=sys.stderr)

        tokens = self.initial_supply
        # print("\n ----- ----- ----->   Starting token count: ", tokens)  print("self.start_inflation: ",
        # self.intervals_till_start_infl)

        self.interval_limit = 75 * 12                         # print("  Interval limit: ", interval_limit)
        self.interval_count_list = [i for i in range(1, self.interval_limit)]    # print(" interval_inflation_rate: ",
                                                            # self.interval_inflation_rate)

        for i in self.interval_count_list:  # print("\n -- Current interval_count: ", interval_count)

            if tokens >= self.stop_inflation:
                self.interval_inflation_rate = self.interval_inflation_rate * (1 - self.deflation_ratio)
                    # mynumber = self.interval_inflation_rate * (1 - self.deflation_ratio)
                    # print("\n\n mynumber: ", mynumber)
                    # print("now in deflation. Interval_inflation is: ", self.interval_inflation_rate)

            tokens = tokens + self.interval_inflation_rate      # print("new count of tokens: ", tokens)
            self.token_count_list.append(tokens)               # print("and we are done with calcs")
            self.ones_list.append(1)
        self.plot_graph(plotfilepath)
        return True

    def plot_graph(self, plotfilepath):
        #print("!!! nms ---------------- plotfilepath: {}".format(plotfilepath), file=sys.stderr)
        # rcParams['figure.figsize'] = [12, 9]
        font = {  'size': 14}
        d = self.deflation_ratio
        inflation = str(self.annual_inflation)
        inter = self.interval_limit / 15
        interlist = []
        x = 0
        while x < self.interval_limit:
            interlist.append(x)
            x += inter

        deflation = "{:.1%}".format(d)
        matplotlib.rc('font', **font)
# ---------------------------------------------- plt
        fig, ax = plt.subplots(figsize=(12, 9))
        intcount = self.interval_count_list
        ax.set_xlim(xmin=interlist[0], xmax=interlist[-1]
        ax.set_ylim(ymin=0, ymax=self.token_count_list[-1])

        print("intcount ", self.token_count_list)
        # self.initial_supply
        # self.interval_count_list






        plt.title('Token Life - Token Supply', pad=20, color="purple", size=30)
        isstr = 'Initial Supply: {}'.format(str(self.initial_supply))

        xlabel_str = "30 day intervals - {} inflation and {} deflation".format(inflation, deflation)
        ylabel_str = self.TOKEN_SYMBOL + ' Tokens in increments of 100 M'
        plt.ylabel(ylabel_str, size=20, color="green", labelpad=20)
        plt.grid(True, linewidth=2, color='green', ds='steps-mid', linestyle='--')
        plt.xlabel(xlabel_str, size=20, labelpad=20, color="blue")
        plt.suptitle("Lifespan for Token " + self.TOKEN_SYMBOL, size=16, y=4, color="red")

        # ----------------new
        import numpy as np
        from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

        # fig = plt.figure()
        # f = plt.figure()
        # ax = fig.add_subplot()
        # Major ticks every 20, minor ticks every 5
        # major_ticks = np.arange(0, 1000, 100)
        # minor_ticks = np.arange(0, 100, 5)

        # ax.set_xticks(major_ticks)
        # ax.set_xticks(minor_ticks, minor=True)
        # ax.set_yticks(major_ticks)
        # ax.set_yticks(minor_ticks, minor=True)
        #
        # # And a corresponding grid
        # ax.grid(which='both')
        #
        # # Or if you want different settings for the grids:
        # ax.grid(which='minor', alpha=0.1, color='green')
        # ax.grid(which='major', alpha=0.1)
#--------------------------new2
        # fig, ax = plt.subplots(figsize=(10, 8))

        # Set axis ranges; by default this will put major ticks every 25.
        # ax.set_xlim(0, 200)
        # ax.set_ylim(0, 200)
        #
        # # Change major ticks to show every 20.
        # ax.xaxis.set_major_locator(MultipleLocator(20))
        # ax.yaxis.set_major_locator(MultipleLocator(20))
        #
        # # Change minor ticks to show every 5. (20/4 = 5)
        # ax.xaxis.set_minor_locator(AutoMinorLocator(4))
        # ax.yaxis.set_minor_locator(AutoMinorLocator(4))
        #
        # # Turn grid on for both major and minor ticks and style minor slightly
        # # differently.
        # ax.grid(which='major', color='#CCCCCC', linestyle='--')
        # ax.grid(which='minor', color='#CCCCCC', linestyle=':')

        plt.plot(self.ones_list, self.token_count_list, color='purple', linestyle=':', linewidth=2)

        plt.legend([isstr, 'Token Initial Supply'], loc='lower left')

        plt.savefig(plotfilepath,  dpi=150, format='svg')
        return True
