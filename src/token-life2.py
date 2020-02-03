
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:53:45 2020

@author: kathynorman
"""

import array as arr
import matplotlib.pyplot as m_pyplot
import win32
import matplotlib
from matplotlib import colors


class NulsPlot(object):
    
    def __init__(self):
        self.token_symbol = "NULS"   # 3 characters, all caps.  e.g SET = Space Exploration 
        # Token
        self.initial_supply = 100000000  #100,000,000  NULS
        self.stop_inflation = 210000000  #210,000,000  NULS
        self.annual_inflation = 5000000   # 5,000,000 NULS
        self.monthly_inflation = self.annual_inflation/12
           #enter your start date, using this format
        self.deflation_ratio = 0.004
        #interval = 30  # inflation/deflation interval in days
        self.start_inflation = 2 * 12
        self.interval_count = 0
        self.tokens = self.initial_supply
        self.token_count = []
        self.token_initial_supply = []
        self.token_interval = []
        self.deflation = False

    def prompt_for_input(self):        
        prompt = True
        while prompt: 
            print('For ' + self.token_symbol + ' the following values are set:')
            print("Initial Supply : " + "{:,}".format(self.initial_supply))
            print('Inflation begins in ' + "{:,}".format(self.start_inflation) + 'months/intervals')
            print('Inflation amount per month/interval: ' +  "{:,}".format(self.monthly_inflation))
            print('Inflation is turned off initial_supply + '
                  'inflation reaches:  ' + "{:,}".format(self.stop_inflation))
            print('De-inflation ratio is: ' + "{:,}".format(self.deflation_ratio))
            print('De-inflation and inflation bgins at the same time.')
        
            prompt_vals = self.prompt_for_value()
            if prompt_vals:
                print(i for i in prompt_vals)
                [self.initial_supply, self.start_inflation, self.monthly_inflation,
                 self.stop_inflation, self.deflation_ratio] = [*prompt_vals]
            self.final_part()
    #% 2d, Portal : % 5.2f" %(1, 05.333))     "{:,}".format(x) 
        # x = float(input("Enter a number:"))
    def prompt_for_value(self)-> []:
           
        start_inflation, deflation_ratio = None, None
        initial_supply, monthly_inflation, stop_inflation = None, None, None

        answer = input('Do you want to change any values? y/n: ')

        if answer == 'n' or answer == 'N':
            return False

        answer = input('Initial Supply : ')

        if answer != "":
            initial_supply = int(float(answer))

        answer = input('Inflation begins in :')
        if answer != "":
            start_inflation = int(float(answer))

        answer = input('Inflation amount per month/interval :')
        if answer != "":
            monthly_inflation = int(float(answer))

        answer = input(
                'Inflation is turned off when total(initial_supply and inflation) '
                'reaches: ')
        if answer != "":
            stop_inflation = int(float(answer))

        answer = input('De-inflation ratio is:  :')
        if answer != "":
            deflation_ratio = float(answer)

        ans_list = [initial_supply, start_inflation, monthly_inflation, stop_inflation,
                deflation_ratio]
        return ans_list
       
    def final_part(self):
        #while True:
    
        #    tokens = (tokens + inflation_amount) * (1 - deflation_ratio)
        if self.tokens >= self.stop_inflation: 
            monthly_inflation = 0
        
        if self.deflation:
           self.monthly_inflation = self.monthly_inflation *  (1 - deflation_ratio)
           
        elif (self.interval_count + 1)  >= self.start_inflation:
           self.deflation = True
        
        self.tokens = self.tokens + self.monthly_inflation
        token_count.append(round(tokens)) 
        token_initial_supply.append(initial_supply)  
        token_interval.append(interval_count)
        interval_count += 1
    
        print(tokens, monthly_inflation, deflation, interval_count)
        
        if interval_count >= 75*12: 
            continue
        
        print("and we are done with calcs")   



if __name__ == "__main__":
    np = NulsPlot()
    np.prompt_for_input()




m_pyplot.gca().set_color_cycle(['blue', 'green'])
plot = m_pyplot.gca()
m_pyplot.set




m_pyplot.suptitle(" Life Span for token " + token_symbol)
m_pyplot.plot(token_interval, token_count)
m_pyplot.plot(token_interval, token_initial_supply)
m_pyplot.legend(['Token Life', 'Token Initial Supply'], loc='upper left')
m_pyplot.ylabel(token_symbol + ' Token Count, increments of 1M')
m_pyplot.xlabel('30 day intervals')
m_pyplot.grid(True)
m_pyplot.show()



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

