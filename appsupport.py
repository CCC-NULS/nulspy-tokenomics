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
        self.annual_inflation = int(args_dict.get("annual_inflation"))  # 5,000,000 NULS
        start_inflation_int = int(args_dict.get("start_inflation"))
        self.real_initial_supply_y = int(args_dict.get("initial_supply_y"))
        plotpath_timestp = args_dict.get("plotpath_timestp")   #
        plotpath_timestp2 = args_dict.get("plotpath_timestp2")   #
        print("max supply: " + str(self.stop_inflation_y))
        print("start_inflation: " + str(start_inflation_int))
        print("annual_inflation: " + str(self.annual_inflation))
        start_disinflation = start_inflation_int + 1
        disinfla_sent = args_dict.get("disinflation_ratio")

        if not disinfla_sent:     # if it's empty  ie == 0
            self.disinflation_ratio = 0
        else:
            self.disinflation_ratio = float(int(disinfla_sent))/1000  # comes as 1-digit whole number

        print("self.disinflation_ratio: " + str(self.disinflation_ratio))
        tokens = self.initial_supply_y

            #  mean length of the Gregorian calendar year is:
            # 1 mean year = (365+1/4-1/100+1/400) days = 365.2425 days    5.2425 /365.2425= 0.0143534774841373
                                # 0.0143534774841373 - subtract this from yearly then divide into intervals
        # new math:
        yrdivisor = 0.0143534774841373  #  5.2425 /365.2425
        annualAdjustedInflationFor360days = self.annual_inflation * yrdivisor
        realcnt = self.annual_inflation - annualAdjustedInflationFor360days
                # 4 must become .4% or .004

        self.interval_limit_x = 30 * 12  # changed 75 to 30 (now 30 years)

        monthly_inflation = realcnt / 12  # 5,000,000 NULS
        old_monthly_inflation = self.annual_inflation / 12  # 5,000,000 NULS
        first_month_inflation = monthly_inflation

        interval_count = 1
        print("new monthly (30.436875 days) inflation: " + str(monthly_inflation))
        print("OLD monthly (30 days) inflation: " + str(old_monthly_inflation))
        print("start inflation: " + str(start_inflation_int))
        print("start disinflation: " + str(start_disinflation))


        print('interval - inflation - tokens')
        spc = '   '
        prev_toks = tokens
        addinf = ' plus inflation '
        minusdis = ' minus disinf: '
        while interval_count <= self.interval_limit_x:

            if (tokens <= self.stop_inflation_y) and (interval_count == start_inflation_int):  # only once, yes inf, no dis
                prev_toks = tokens
                new_monthly_inflation = monthly_inflation
                tokens = prev_toks + monthly_inflation

                new_mon_infln_str = "{:,}".format(round(new_monthly_inflation)) + minusdis

                intct = str(interval_count) + spc
                prevtokst = "{:,}".format(round(prev_toks)) + addinf
                newtoken_fmt_str = "{:,}".format(round(tokens)) + spc

                disin_amt_str = "0  = "
                ps1 = '   ' + str(monthly_inflation) + ' - ' + disin_amt_str + ' = ' + new_monthly_inflation

                pstring = intct + prevtokst + new_mon_infln_str +  newtoken_fmt_str

                print(pstring)
                monthly_inflation = new_monthly_inflation
            elif (tokens <= self.stop_inflation_y) and (interval_count >= start_inflation_int): # yes inflation
                prev_toks = tokens
                new_monthly_inflation = monthly_inflation * (1 - self.disinflation_ratio)
                dis_amt = monthly_inflation - new_monthly_inflation
                tokens = prev_toks + new_monthly_inflation

                intct = str(interval_count) + spc
                prevtokst = "{:,}".format(round(prev_toks)) + addinf
                new_mon_infln_str = "{:,}".format(round(new_monthly_inflation)) + '  '
                disin_amt_str = "{:,}".format(round(dis_amt)) + '  = '
                newtoken_fmt_str = "{:,}".format(round(tokens)) + spc
                ps1 = '   ' + str(monthly_inflation) + ' - ' + disin_amt_str + ' = ' + new_monthly_inflation
                pstring = intct + prevtokst + new_mon_infln_str + newtoken_fmt_str

                print(ps1)
                print(pstring)
                monthly_inflation = new_monthly_inflation
            else:
                # print(str(interval_count) + '               ' + str("{:,}".format(round(tokens))))
                intct = str(interval_count) + spc
                prevtokst = str(prev_toks) + addinf
                new_mon_infln_str = str(0) + minusdis
                newtoken_fmt_str = ' 0 '

                disin_amt_str = "0   = "
                pstring = intct + prevtokst + new_mon_infln_str + disin_amt_str + newtoken_fmt_str
                print(pstring)

            self.token_count_list_y.append(round(tokens, 0))
            self.initial_supply_list.append(self.initial_supply_y)
            self.token_interval_list.append(interval_count)
            interval_count += 1
        tresult = self.plot_graph(plotpath_timestp, plotpath_timestp2)
        return tresult

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

    def plot_graph(self, plotpath_timed, plotpath_timed2):
        plt.ioff()
        font = {'size': 11}
        stp_inf = self.stop_inflation_y
        dtt = str(datetime.now())
        dt = dtt[0:-7]
        nulsattrib = ' Plot by NULS Tokenlife'
        dt = dt + nulsattrib
        
        disinflation_ratio = self.disinflation_ratio
        disinflation = "{:.01%}".format(disinflation_ratio)
        initial_sup_formatted = "{:,}".format(self.initial_supply_y)
        stp_inf_formatted = "{:,}".format(self.stop_inflation_y)

        max_text = 'Max Supply = ' + str(stp_inf_formatted)

        plt.margins(x=.1, y=.001, tight=False)

        top_x = int(self.interval_limit_x)
        bottom_y = self.initial_supply_y
        top_count = self.token_count_list_y[-1]
        top_y = int(top_count)
        vpadding = top_y / 20
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
        plt.text(100, ylocation, '---- Token Growth in 360 Intervals (~ 30 yrs)', color='purple', size='x-large',
                 weight='bold')


        # -- -- -- -- TICKS -- -- -- -- -- -- --  #

        gx = int(top_x / 10)
        major_x_gaps = self.round_up_to_multiple(gx, 50)  # was 100
        major_ticks_x = np.arange(0, top_x, major_x_gaps)

        gy = int(top_y / 10)
        major_y_gaps = self.round_up_to_multiple(gy, 10000)  # was 1000000
        major_ticks_y = np.arange(bottom_y, top_y, major_y_gaps)

        big_x = top_x + top_x/10

        big_y = top_y + top_y/10
        ax.set_xlim(xmin=0, xmax=big_x)
        ax.set_ylim(ymin=bottom_y, ymax=big_y)

        ax.set_yticks(major_ticks_y)
        ax.set_xticks(major_ticks_x)
        ax.ticklabel_format(style='plain')

        ax.grid(which='both')

        # an_infl = str("{:,}".format(round(self.annual_inflation / 12)))
        an_infl = str("{:,}".format(self.annual_inflation))

        ylabel_str = 'Total Supply'

        plt.ylabel(ylabel_str, size=14, color="green", labelpad=7)
        spacer = "                       "
        bottom_str_top = "  Initial Supply: " + initial_sup_formatted + "     Max Supply: " + str(stp_inf_formatted)
        bottom_str_bottom = spacer + "30 day Intervals, Annual Inflation: " + an_infl + ", Disinflation: " + disinflation
        plt.figtext(0.1, 0.05, bottom_str_bottom,  color='b',  size=11, weight='bold')  # bottom lines
        plt.figtext(0.007, 0.007, dt,  color='b',  size=7)   # datestamp left bottom

        plt.xlabel(bottom_str_top, size=14, labelpad=20, color="blue", weight="bold")

        plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))  # No decimal places

        plt.title('Life Span for Token', pad=20, color="purple", size=30)
        plt.suptitle("Lifespan for Token " + self.TOKEN_SYMBOL, size=14, y=4, color="red")

        plt.plot(self.token_count_list_y, color='purple', linestyle='-', linewidth=3)

        # plt.savefig(plotpath_generic,  dpi=150, format='svg')
        plt.savefig(plotpath_timed,  dpi=150, format='svg')
        plt.savefig(plotpath_timed2,  dpi=150, format='svg')
        #plt.show()
        return True


        # supply_label = str("{:,}".format(self.real_initial_supply_y))
        # plt.legend(['', str1], loc='lower center')
        # str1 = 'Token Growth Over Time'
        # ax.annotate('Stop Inflation Boundary', (25, text_loc))
