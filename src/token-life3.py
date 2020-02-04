# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:53:45 2020
@author: kathynorman
"""

import matplotlib.pyplot as plt

from matplotlib.axes import Axes
import matplotlib.axes
import win32


# Token      #enter your start date, using this format       #interval = 30  #
# inflation/deflation interval in days


class NulsPlot(object):

    def __init__(self):
        self.TOKEN_SYMBOL = "VKG"  # 3 characters, all caps.  e.g SET = Space Exploration
        self.initial_supply = 100000000  # 100,000,000  NULS
        self.stop_inflation = 210000000  # 210,000,000  NULS
        self.deflation_ratio = 0.004
        self.annual_inflation = 5000000  # 5,000,000 NULS
        self.interval_inflation_tokens = self.annual_inflation / 12  # 5,000,000 NULS

        self.start_inflation = 2 * 12
        self.token_count_list = []
        self.interval_count_list = []

    def main(self):
        print('\nFor ' + self.TOKEN_SYMBOL + ' the following values are set:')  # 1

        print("Initial Supply : " + "{:,}".format(self.initial_supply))  # 2

        print('Inflation begins in ' + "{:,}".format(self.start_inflation) + ' intervals')  # 3

        print('Inflation tokens per interval: ' + "{:,}".format(self.interval_inflation_tokens))
        print('Inflation is turned off self.start_inflation when inflation reaches:  ' +
              "{:,}".format(self.stop_inflation))
        print('De-inflation ratio is: ' + "{:,}".format(self.deflation_ratio))
        print('De-inflation and inflation begin at the same time.')

        answer = input('\n----->  Do you want to change any values? (y/n): ')

        if answer == 'n' or answer == 'N':
            self.final_part()  # go directly to end
        else:
            self.get_new_vals()  # intermediary step

    def get_new_vals(self) -> []:

        answer = input('Initial Supply : ')
        if answer != "":
            self.start_inflation = int(float(answer))

        answer = input('Inflation begins in :')
        if answer != "":
            self.start_inflation = int(float(answer))

        answer = input('Inflation amount per month/interval :')
        if answer != "":
            self.interval_inflation_tokens = int(float(answer))

        inflat_words = 'Inflation is turned off when total (self.start_inflation and inflation) reaches: '
        answer = input(inflat_words)
        if answer != "":
            self.stop_inflation = int(float(answer))

        answer = input('De-inflation ratio is:  :')
        if answer != "":
            self.deflation_ratio = float(answer)

        self.final_part()

    def final_part(self):

        tokens = self.initial_supply
        print("\n ----- ----- ----->   Starting token count: ", tokens)
        print("self.start_inflation: ", self.start_inflation)

        interval_limit = 75 * 12
        print("  Interval limit: ", interval_limit)
        self.interval_count_list = [i for i in range(1, interval_limit)]
        print(" interval_inflation_tokens: ", self.interval_inflation_tokens)

        for interval_count in self.interval_count_list:
            print("\n -- Current interval_count: ", interval_count)

            if tokens >= self.stop_inflation:
                mynumber = self.interval_inflation_tokens * (1 - self.deflation_ratio)
                print("\n\n mynumber: ", mynumber)
                self.interval_inflation_tokens = self.interval_inflation_tokens * (1 - self.deflation_ratio)
                print("now in deflation. Interval_inflation is: ", self.interval_inflation_tokens)

            tokens = tokens + self.interval_inflation_tokens
            print("new count of tokens: ", tokens)
            self.token_count_list.append(tokens)

            print("\n\n")

        print("and we are done with calcs")
        self.plot_graph()

    def plot_graph(self):
        # token_count_list, token_self.start_inflation, interval_count_list
        # token_interval = [i for i in range(1, token_intv+1)]
        #
        # plt.legend(['Token Life', 'Token Initial Supply'], loc='upper left')
        #
        xlabel_str = '30 day intervals'
        # ylabel_str = self.TOKEN_SYMBOL + ' Token Count, increments of 1M'

        #
        # plt.ylabel(ylabel_str)
        # plt.xlabel(xlabel_str)
        # plt.suptitle(" Life Span for token " + self.TOKEN_SYMBOL)
        # plt.grid(True)
        # plt.plot(token_interval, token_count_lst, token_self.start_inflation )
        plt.xlabel(xlabel_str)
        plt.suptitle(" Life Span for token " + self.TOKEN_SYMBOL)
        plt.plot(self.interval_count_list, self.token_count_list)
        plt.show()

        # x = [1,2,3]
        # y = [3,4,5]
        # plt.plot(x, y,  label=xlab, color='green', linestyle=':', )
        # plt.show()


if __name__ == "__main__":
    np = NulsPlot()
    np.main()

    # The set_color_cycle attribute was deprecated in version 1.5.
    # Use set_prop_cycle instead.