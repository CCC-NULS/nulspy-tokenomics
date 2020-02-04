
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
            annual_inflation = 5000000  # 5,000,000 NULS
            monthly_inflation = annual_inflation / 12
            start_inflation = 2 * 12
            print('\nFor ' + self.token_symbol + ' the following values are set:')
            print("Initial Supply : " + "{:,}".format(initial_supply))
            print('Inflation begins in ' + "{:,}".format(start_inflation) + ' months/intervals')
            verbs = 'Inflation amount per month/interval: '
            mo_inflat = round(monthly_inflation)
            print(verbs + "{:,}".format(mo_inflat))
            inf = annual_inflation * .000001
            print("Annual inflation percent: " + str(inf) + '%')



            words = 'Inflation is turned off when initital supply + inflation reaches '
            print(words + "{:,}".format(stop_inflation))
            print('De-inflation ratio is: ' + "{:,}".format(deflation_ratio))
            print('De-inflation and inflation begin at the same time')
            orig_list = [initial_supply, start_inflation, monthly_inflation, stop_inflation,
                         deflation_ratio]
            answer = input('\n----->  Do you want to change any values? (y/n): ')
            if answer == 'n' or answer == 'N':
                self.final_part(orig_list)
            else:
                new_vals = self.get_new_vals(orig_list)
                self.final_part(new_vals)

    def get_new_vals(self, the_list) -> []:
        [initial_supply, start_inflation, monthly_inflation, stop_inflation,
         deflation_ratio] = [*the_list]

        answer = input('Initial Supply : ')
        inf = monthly_inflation * 12 * .000001
        print("Annual inflation percent: " + str(inf) + '%')

        if answer != "":
            initial_supply = int(float(answer))

        answer = input('Inflation begins in :')
        if answer != "":
            start_inflation = int(float(answer))

        answer = input('Inflation amount per month/interval :')
        if answer != "":
            monthly_inflation = int(float(answer))

        inflat_words = 'Inflation is turned off when total (initial_supply and inflation) reaches: '
        answer = input(inflat_words)
        if answer != "":
            stop_inflation = int(float(answer))

        answer = input('De-inflation ratio is:  :')
        if answer != "":
            deflation_ratio = float(answer)

        ans_list = [initial_supply, start_inflation, monthly_inflation, stop_inflation,
                    deflation_ratio]
        return ans_list
       
    def final_part(self, pvals):
        [initial_supply, start_inflation, monthly_inflation, stop_inflation, deflation_ratio] = \
            [*pvals]
        tokens = initial_supply  # start for tokens

        tokens = tokens + monthly_inflation
        tokens_plus_inflation_rounded = []
        token_count = []
        token_initial_supply = []

        # token_count = initial_supply
        deflation = False
        interval_count = 5
        interval_count_list = []
        monthly_inflation_list = []

        for i in range(interval_count):
            if tokens >= stop_inflation:
                monthly_inflation = 0

            if deflation:
                monthly_inflation = monthly_inflation * (1 - deflation_ratio) / 1000000

            elif (interval_count + 1) >= start_inflation:
                deflation = True

            tokens_plus_inflation = tokens + monthly_inflation
            tokens_plus_inflation_round = round(tokens_plus_inflation)

            print("\n\ninitial_supply: ", round(initial_supply))
            print("tokens plus inflation (rounded): ", tokens_plus_inflation_round)
            print("monthly_inflation: ", monthly_inflation)
            print("deflation: ", deflation )
            print("interval_count: ", interval_count)

            monthly_inflation_list.append(monthly_inflation)
            tokens_plus_inflation_rounded.append(tokens_plus_inflation_round)

            token_initial_supply.append(initial_supply)
            interval_count_list.append(interval_count)
            interval_count += 1
            initial_supply = tokens_plus_inflation

            if interval_count >= 75*12:
                pass

        tok_list = [*token_count, *token_initial_supply, interval_count]

        print("and we are done with calcs")
        self.plot_graph(tok_list)

    def plot_graph(self, toks_list):
        [token_count, token_initial_supply, token_interval] = [*toks_list]
        fa = '7'
        fb = '5'
        fstr: str = 'figsize = (' + fa + ', ' + fb + ')'
        plt.figure(fstr)
        legend_str = "Life Span for token " + self.token_symbol
        plt.legend(legend_str)

        xlab = '30 day intervals'

        ylab = self.token_symbol + ' Token Count: increments of 1M'
        plt.title = 'Go Vikings!'
        plt.ylabel(ylab)
        x = [1,2,3]
        y = [3,4,5]
        plt.plot(x, y,  label=xlab, color='green', linestyle=':', )
        plt.show()


        # ax.plot(token_interval, token_count, 'blue')
        # ax.plot(token_interval, token_initial_supply, 'green')
        # ax.legend(['Token Life', 'Token Initial Supply'], loc='bottom right')
        # ax.ylabel = self.token_symbol + ' Token Count, increments of 1M'
        # ax.xlabel = ' 30 day intervals'
        # ax.grid(True)
        # ax.plot
        # ax.show()



if __name__ == "__main__":
    np = NulsPlot()
    np.main()

    # The set_color_cycle attribute was deprecated in version 1.5.
    # Use set_prop_cycle instead.

"""
sample code to be deleted later   

import matplotlib.pyplot as m_pyplot
m_pyplot.plot([1, 2, 3, 4])
m_pyplot.ylabel('some numbers')
m_pyplot.show()


import matplotlib.pyplot as m_pyplot

m_pyplot.plot(range(10))  # Creates the plot.  No need to save the current figure.
m_pyplot.draw()  # Draws, but does not block

m_pyplot.figure()  # New window, if needed.  No need to save it, as pyplot uses the concept of current figure
m_pyplot.plot(range(10, 20))
m_pyplot.draw()




import array as arr
a = arr.array('i', [2, 4, 6, 8])
print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-1])

try:
     coinN= int(input("Enter next coin: "))

     if coinN == "" and totalcoin == rand: 
         print("Congratulations. Your calculations were a success.")
     if coinN == "" and totalcoin < rand:
         print("I'm sorry. You only entered",totalcoin,"cents.")  

 except ValueError:
     print("Invalid Input")
 else:
     totalcoin = totalcoin + coinN
"""

