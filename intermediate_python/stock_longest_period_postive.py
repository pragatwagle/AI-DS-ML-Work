# Program that finds the longest period a stock was up in 2020.
# Date: 07/11/2021
# Author: Pragat Wagle

import numpy as np
import yfinance as yf
import pandas as pd
import math
from math import sqrt

def max_up(stock):
    print("\nThe longest up period for the stock symbol IBM: ")
    longestPeriod = 0
    length = len(stock['Close']) - 1 
    stockData = stock.reset_index()
    longestTempPeroid = 0
    startTempDate = 0
    endTempDate = 0
    valueAtStart = 0
    valueAtEnd = 0
    for i in range(length):
       
        if(stock['Close'][i] <= stock['Close'][i+1]):
            longestTempPeroid+=1
        else:
            longestTempPeroid = 0
            
        if(longestTempPeroid > longestPeriod):
                longestPeriod = longestTempPeroid
                endTempDate = stockData['Date'][i+1]
                startTempDate = stockData['Date'][i-longestPeriod+1]
                valueAtStart = stock['Close'][i-longestPeriod+1]
                valueAtEnd = stock['Close'][i+1]
    
    startDate = startTempDate.date()
    endDate = endTempDate.date()
    valueAtStart = str(round(valueAtStart, 2))
    valueAtEnd = str(round(valueAtEnd, 2))
    print("Length in days:              " + str(longestPeriod))
    print("Period started on:           " + str(startDate).rjust(10))
    print("Close stock value at start:  " + str(endDate).rjust(5))
    print("Period ended on:             " + valueAtStart)
    print("Close stock value at end:    " + valueAtEnd)


def main():
    print("Program that finds the longest period a stock was up in 2020.\n")
    stock = input("Please enter the stock symbol: ")
    stockData = yf.download(stock, start = '2020-01-01', end='2021-01-01', progress = False)
    max_up(stockData)
  
main()





















