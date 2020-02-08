# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:53:45 2020
@author: Kathy Norman and Nancy Schorr
"""
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib


class AppSupport:
    def __init__(self):
        self.TOKEN_SYMBOL = "VKG"  # 3 characters, all caps.  e.g SET = Space Exploration
        self.initial_supply = 0  # 100,000,000  NULS
        self.stop_inflation = 0  # 210,000,000  NULS
        self.deflation_ratio = 0
        self.annual_inflation = 0  # 5,000,000 NULS
        self.intervals_till_start_infl = 0
        self.interval_inflation_rate_list = self.annual_inflation / 12  # 5,000,000 NULS
        self.token_count_list = []
        self.interval_count_list = []
        self.interval_supply_list = [i for i in range(1, 900)]
        self.interval_inflation_rate = None

    def main(self, args_dict):
        self.initial_supply = int(args_dict.get("ini_sup"))  # 100,000,000  NULS
        self.stop_inflation = int(args_dict.get("stop_i"))   # 210,000,000  NULS
        self.deflation_ratio = float(args_dict.get("defl"))
        self.annual_inflation = int(args_dict.get("ann_inf"))  # 5,000,000 NULS
        self.intervals_till_start_infl = int(args_dict.get("inf_interval"))
        self.interval_inflation_rate = self.annual_inflation / 12  # 5,000,000 NULS
        plotfilepath = args_dict.get("plotfilepath")

        tokens = self.initial_supply
        # print("\n ----- ----- ----->   Starting token count: ", tokens)  print("self.start_inflation: ",
        # self.intervals_till_start_infl)

        interval_limit = 75 * 12                         # print("  Interval limit: ", interval_limit)
        self.interval_count_list = [i for i in range(1, interval_limit)]    # print(" interval_inflation_rate: ",
                                                            # self.interval_inflation_rate)

        for i in self.interval_count_list:  # print("\n -- Current interval_count: ", interval_count)

            if tokens >= self.stop_inflation:
                self.interval_inflation_rate = self.interval_inflation_rate * (1 - self.deflation_ratio)
                    # mynumber = self.interval_inflation_rate * (1 - self.deflation_ratio)
                    # print("\n\n mynumber: ", mynumber)
                    # print("now in deflation. Interval_inflation is: ", self.interval_inflation_rate)

            tokens = tokens + self.interval_inflation_rate      # print("new count of tokens: ", tokens)
            self.token_count_list.append(tokens)               # print("and we are done with calcs")
        self.plot_graph(plotfilepath)
        return True

    def plot_graph(self, plotfilepath):
        from time import sleep
        font = {'weight': 'bold',
                'size': 15}
        d = self.deflation_ratio
        inflation = str(self.annual_inflation)

        deflation = "{:.1%}".format(d)
        matplotlib.rc('font', **font)
        rcParams['figure.figsize'] = [12, 9]

        plt.title('Token Life - Token Supply')
        isstr = 'Initial Supply: {}'.format(str(self.initial_supply))
        print(isstr)

        plt.legend([isstr, 'Token Initial Supply'], loc='lower right')
        xlabel_str = "30 day intervals - {} inflation and {} deflation".format(inflation, deflation)
        ylabel_str = self.TOKEN_SYMBOL + ' Tokens in increments of 1M'
        plt.ylabel(ylabel_str, size=16, color="green")
        plt.grid(True, linewidth=2, color='green')
        plt.xlabel(xlabel_str, labelpad=20)
        plt.suptitle("Lifespan for Token " + self.TOKEN_SYMBOL, size=16, y=1.12, color="red")
        # ax2 = plt
        # r = rcParams

        plt.plot(self.interval_count_list, self.token_count_list, color='purple', linestyle='--', linewidth=5)
        # plt.plot(self.interval_count_list, self.interval_inflation_rate_list, color='orange', linestyle='--', linewidth=5)
        print("now path is: ", plotfilepath)
        plt.savefig(plotfilepath,  dpi=150, format='svg')
        sleep(3)
        return True
