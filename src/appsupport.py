# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:53:45 2020
@author: Kathy Norman and Nancy Schorr
"""
from waitress import serve
from flask import Flask, request, render_template, redirect, url_for
from jinja2 import Environment, PackageLoader, select_autoescape
import appsupport
from datetime import datetime
from os import path

import matplotlib.pyplot as plt


class AppSupport:
    def __init__(self):
        self.TOKEN_SYMBOL = "VKG"  # 3 characters, all caps.  e.g SET = Space Exploration
        self.initial_supply = 100000000  # 100,000,000  NULS
        self.stop_inflation = 210000000  # 210,000,000  NULS
        self.deflation_ratio = 0.004
        self.annual_inflation = 5000000  # 5,000,000 NULS
        self.intervals_till_start_infl = 24
        self.interval_inflation_rate = self.annual_inflation / 12  # 5,000,000 NULS
        self.token_count_list = []
        self.interval_count_list = []
        self.pname = None
        self.img_tag = None

    def main(self, args_dict):
        self.TOKEN_SYMBOL = "VKG"  # 3 characters, all caps.  e.g SET = Space Exploration

        self.initial_supply = int(args_dict.get("ini_sup"))  # 100,000,000  NULS
        self.stop_inflation = int(args_dict.get("stop_i"))   # 210,000,000  NULS
        self.deflation_ratio = float(args_dict.get("defl"))
        self.annual_inflation = int(args_dict.get("ann_inf"))  # 5,000,000 NULS
        self.intervals_till_start_infl = int(args_dict.get("inf_interval"))
        self.img_tag = args_dict.get("img_tag")
        fname = args_dict.get("fname")
        self.pname = args_dict.get("pname")
        self.interval_inflation_rate = self.annual_inflation / 12  # 5,000,000 NULS

        tokens = self.initial_supply
        print("\n ----- ----- ----->   Starting token count: ", tokens)
        print("self.start_inflation: ", self.intervals_till_start_infl)

        interval_limit = 75 * 12
        print("  Interval limit: ", interval_limit)
        self.interval_count_list = [i for i in range(1, interval_limit)]
        print(" interval_inflation_rate: ", self.interval_inflation_rate)

        for interval_count in self.interval_count_list:
            print("\n -- Current interval_count: ", interval_count)

            if tokens >= self.stop_inflation:
                mynumber = self.interval_inflation_rate * (1 - self.deflation_ratio)
                print("\n\n mynumber: ", mynumber)
                self.interval_inflation_rate = self.interval_inflation_rate * (1 - self.deflation_ratio)
                print("now in deflation. Interval_inflation is: ", self.interval_inflation_rate)

            tokens = tokens + self.interval_inflation_rate
            print("new count of tokens: ", tokens)
            self.token_count_list.append(tokens)
            print("\n\n")
        print("and we are done with calcs")
        self.plot_graph(fname)
        return True

    def plot_graph(self, fname):

        plt.title('Token Life - Token Supply')
        plt.legend(['Initial Supply: ', self.initial_supply], loc='upper left')
        #
        xlabel_str = '30 day intervals'
        ylabel_str = self.TOKEN_SYMBOL + ' Token Count, increments of 1M'
        plt.ylabel(ylabel_str)
        plt.grid(True)
        plt.xlabel(xlabel_str)
        plt.xlabel("yes")
        plt.suptitle(" Life Span for token " + self.TOKEN_SYMBOL)
        plt.plot(self.interval_count_list, self.token_count_list)
        plt.savefig(fname,  dpi=150, format='svg')
        return True

