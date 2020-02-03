 
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:53:45 2020

@author: kathynorman
"""

import array as arr
import matplotlib.pyplot as plt


token_symbol = "NULS"   # 3 characters, all caps.  e.g SET = Space Exploration Token
initial_supply = 100000000  #100,000,000  NULS
stop_inflation = 210000000  #210,000,000  NULS
annual_inflation = 5000000   # 5,000,000 NULS
monthly_inflation = annual_inflation/12

   #enter your start date, using this format
deflation_ratio = 0.004
#interval = 30  # inflation/deflation interval in days
start_inflation = 2 * 12


interval_count = 0
tokens = initial_supply
token_count = []
token_initial_supply = []
token_interval = []

deflation = False


def prompt_for_input():
    
    global token_symbol, initial_supply, monthly_inflation, stop_inflation
    
    
    prompt = True
    while prompt: 
        print('For ' + token_symbol + ' the following values are set:')
        print('Initial Supply : ' +   "{:,}".format(initial_supply))
        print('Inflation begins in ' + "{:,}".format(start_inflation) + ' months/intervals')
        print('Inflation amount per month/interval: ' +  "{:,}".format(monthly_inflation))
        print('Inflation is turned off initial_supply + inflation reaches:  ' +  "{:,}".format(stop_inflation))
        print('De-inflation ratio is: ' +  "{:,}".format(deflation_ratio))
        print('De-inflation and inflation bgins at the same time.')
    
        prompt = prompt_for_value()
        print(prompt)
        
        
#% 2d, Portal : % 5.2f" %(1, 05.333))     "{:,}".format(x) 
    # x = float(input("Enter a number:"))
def prompt_for_value():
       
        global token_symbol, initial_supply, monthly_inflation, stop_inflation  

        answer = input('Do you want to change any values? y/n: ')
        if answer == 'n' or answer == 'N' : return False

        answer = input('Initial Supply : ')
        if answer != "": initial_supply = int(float(answer))
        answer = input('Inflation begins in :')
        if answer !=  "": start_inflation = int(float(answer))
        answer = input('Inflation amount per month/interval :')
        if answer !=  "": monthly_inflation = int(float(answer))        
        answer = input('Inflation is turned off when total(initial_supply and inflation) reaches: ')
        if answer !=  "": stop_inflation = int(float(answer))           
        answer = input('De-inflation ratio is:  :')
        if answer !=  "": deflation_ratio = float(answer)   
       

prompt_for_input()


while True:
    
#    tokens = (tokens + inflation_amount) * (1 - deflation_ratio)
    if tokens >= stop_inflation: monthly_inflation = 0
    
    if deflation:
       monthly_inflation = monthly_inflation *  (1 - deflation_ratio)
    elif (interval_count + 1)  >= start_inflation:
       deflation = True
    
    tokens = tokens + monthly_inflation
    token_count.append(round(tokens)) 
    token_initial_supply.append(initial_supply)  
    token_interval.append(interval_count)
    interval_count += 1

    print(tokens, monthly_inflation, deflation, interval_count)
    if interval_count >= 75*12 : break
    
print("and we are done")   




plt.gca().set_color_cycle(['blue', 'green'])

plt.suptitle(" Life Span for token " + token_symbol)
plt.plot(token_interval, token_count )
plt.plot(token_interval, token_initial_supply )
plt.legend(['Token Life', 'Token Initial Supply'], loc='upper left')
plt.ylabel(token_symbol + ' Token Count, increments of 1M')
plt.xlabel('30 day intervals')
plt.grid(True)
plt.show()



"""
sample code to be deleted later   

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()


import matplotlib.pyplot as plt

plt.plot(range(10))  # Creates the plot.  No need to save the current figure.
plt.draw()  # Draws, but does not block

plt.figure()  # New window, if needed.  No need to save it, as pyplot uses the concept of current figure
plt.plot(range(10, 20))
plt.draw()




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

