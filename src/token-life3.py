
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
        self.token_symbol = "VKG"   # 3 characters, all caps.  e.g SET = Space Exploration

    def main(self):
        prompt = True
        while prompt:
            deflation_ratio = 0.004
            initial_supply = 100000000  # 100,000,000  NULS
            stop_inflation = 210000000  # 210,000,000  NULS
            interval_inflation = 5000000  # 5,000,000 NULS
            start_inflation = 2 * 12
            print('\nFor ' + self.token_symbol + ' the following values are set:') #1

            print("Initial Supply : " + "{:,}".format(initial_supply)) #2

            print('Inflation begins in ' + "{:,}".format(start_inflation) + ' intervals') #3

            print('Inflation amount per interval: ' + "{:,}".format(interval_inflation))
            print('Inflation is turned off initial_supply when inflation reaches:  ' +
                  "{:,}".format(stop_inflation))
            print('De-inflation ratio is: ' + "{:,}".format(deflation_ratio))
            print('De-inflation and inflation begin at the same time.')

            answer = input('\n----->  Do you want to change any values? (y/n): ')

            orig_list = [initial_supply, start_inflation, interval_inflation, stop_inflation,
                         deflation_ratio]

            if answer == 'n' or answer == 'N':
                self.final_part(orig_list)
            else:
                new_vals = self.get_new_vals(orig_list)
                self.final_part(new_vals)

    def get_new_vals(self, the_list) -> []:
        [initial_supply, start_inflation, interval_inflation, stop_inflation,
         deflation_ratio] = [*the_list]

        answer = input('Initial Supply : ')
        inf = interval_inflation * 12 * .000001
        print("Annual inflation percent: " + str(inf) + '%')

        if answer != "":
            initial_supply = int(float(answer))

        answer = input('Inflation begins in :')
        if answer != "":
            start_inflation = int(float(answer))

        answer = input('Inflation amount per month/interval :')
        if answer != "":
            interval_inflation = int(float(answer))

        inflat_words = 'Inflation is turned off when total (initial_supply and inflation) reaches: '
        answer = input(inflat_words)
        if answer != "":
            stop_inflation = int(float(answer))

        answer = input('De-inflation ratio is:  :')
        if answer != "":
            deflation_ratio = float(answer)

        answer_list = [initial_supply, start_inflation, interval_inflation, stop_inflation,
                       deflation_ratio]
        return answer_list
       
    def final_part(self, pvals):
        [initial_supply, start_inflation, interval_inflation, stop_inflation, deflation_ratio] = [
            *pvals]

        deflation = False
        interval_count = 0
        tokens = initial_supply
        token_count = []
        token_initial_supply = []
        token_interval = []


        while True:
            if tokens >= stop_inflation:
                interval_inflation = 0

            if deflation:
                interval_inflation = interval_inflation * (1 - deflation_ratio)
            elif (interval_count + 1) >= start_inflation:
                deflation = True

            tokens = tokens + interval_inflation
            token_count.append(round(tokens))
            token_initial_supply.append(initial_supply)
            token_interval.append(interval_count)
            interval_count += 1

            print(tokens, interval_inflation, deflation, interval_count)
            print("\n\ninterval_count: ", interval_count)
            print("initial_supply: ", round(initial_supply))
            print("interval inflation: ", round(interval_inflation))
            print("deflation: ", deflation)

            if interval_count >= 75 * 12:   #put this back
            #if interval_count >= 12:
                break

        tok_list = [token_count, token_initial_supply, interval_count]

        print("and we are done with calcs")
        self.plot_graph(tok_list)

    def plot_graph(self, toks_list):
        [token_count, token_initial_supply, token_intv] = [*toks_list]
        token_interval = [i for i in range(1, token_intv+1)]

        plt.legend(['Token Life', 'Token Initial Supply'], loc='upper left')

        xlabel_str = '30 day intervals'
        ylabel_str = self.token_symbol + ' Token Count, increments of 1M'

        figtup = ('7', '5',)
        fstr: str = 'figsize = (' + figtup[0] + ', ' + figtup[0] + ')'
        plt.figure(fstr)

        plt.ylabel(ylabel_str)
        plt.xlabel(xlabel_str)
        plt.suptitle(" Life Span for token " + self.token_symbol)
        plt.grid(True)
        plt.plot(token_interval, token_count, color="green")
        plt.plot(token_interval, token_initial_supply, color="blue")

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
