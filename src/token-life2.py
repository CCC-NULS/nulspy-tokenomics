
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:53:45 2020

@author: kathynorman
"""

import matplotlib.pyplot as mpyplot
from matplotlib.axes import Axes
import win32

# Token      #enter your start date, using this format       #interval = 30  #
# inflation/deflation interval in days


class NulsPlot(object):
    
    def __init__(self):
        self.token_symbol = "NULS"   # 3 characters, all caps.  e.g SET = Space Exploration

    def main(self):
        prompt = True
        while prompt:
            deflation_ratio = 0.004
            initial_supply = 100000000  # 100,000,000  NULS
            stop_inflation = 210000000  # 210,000,000  NULS
            annual_inflation = 5000000  # 5,000,000 NULS
            monthly_inflation = annual_inflation / 12
            start_inflation = 2 * 12
            print('For ' + self.token_symbol + ' the following values are set:')
            print("Initial Supply : " + "{:,}".format(initial_supply))
            print('Inflation begins in ' + "{:,}".format(start_inflation) + ' months/intervals')
            verbs = 'Inflation amount per month/interval: '
            print(verbs + "{:,}".format(monthly_inflation))
            words = 'Inflation is turned off initial_supply + '
            print(words + 'inflation reaches:  ' + "{:,}".format(stop_inflation))
            print('De-inflation ratio is: ' + "{:,}".format(deflation_ratio))
            print('De-inflation and inflation begin at the same time.')
            orig_list = [initial_supply, start_inflation, monthly_inflation, stop_inflation,
                        deflation_ratio]
            answer = input('Do you want to change any values? y/n: ')
            if answer == 'n' or answer == 'N':
                self.final_part(orig_list)
            else:
                new_vals = self.get_new_vals(orig_list)
                self.final_part(new_vals)

    def get_new_vals(self, the_list) -> []:
        [initial_supply, start_inflation, monthly_inflation, stop_inflation,
         deflation_ratio] = [*the_list]

        answer = input('Initial Supply : ')

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
        token_count = []
        token_initial_supply = []
        token_interval = []

        # token_count = initial_supply
        deflation = False
        interval_count = 0

        if tokens >= stop_inflation:
            monthly_inflation = 0
        
        if deflation:
            monthly_inflation = monthly_inflation * (1 - deflation_ratio)
           
        elif (interval_count + 1) >= start_inflation:
            deflation = True
        
        tokens = tokens + monthly_inflation
        tokens_rounded = round(tokens)

        token_count.extend([tokens_rounded])

        token_initial_supply.append(initial_supply)  
        token_interval.append(interval_count)
        interval_count += 1

        print("tokens: ", tokens )
        print("monthly_inflation: ", monthly_inflation,)
        print("deflation: ", deflation, )
        print("interval_count: ", interval_count)

        if interval_count >= 75*12: 
            pass

        tok_list = [*token_count, *token_initial_supply, token_interval]

        print("and we are done with calcs")
        self.plot_graph(tok_list)

    def plot_graph(self, toks_list):
        [token_count, token_initial_supply, token_interval] = [*toks_list]
        m_pyplot = mpyplot.gca()
        y0 = 0
        width = 2
        height = 5
        rect = [y0, width, height]
        ax = Axes(m_pyplot, rect)

        ax.legend("Life Span for token " + self.token_symbol)
        ax.plot(token_interval, token_count, 'blue')
        ax.plot(token_interval, token_count)
        ax.plot(token_interval, token_initial_supply)
        ax.legend(['Token Life', 'Token Initial Supply'], loc='upper left')
        ax.ylabel = 'self.token_symbol + ' + 'Token Count, increments of 1M'
        ax.xlabel = '30 day intervals'
        ax.grid(True)
        ax.legend = "ax.legend"
        ax.plot
        ax.show()



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

