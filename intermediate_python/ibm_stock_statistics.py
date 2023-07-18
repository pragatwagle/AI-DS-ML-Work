# Program that calculates IBM stock data statistics for year 2020.
# Date: 07/11/2021
# Author: Pragat Wagle

import numpy as np
import yfinance as yf
import math

def main():
    print("Program that calculates IBM stock data statistics for year 2020.")
    stocks = yf.download('ibm', start = '2020-01-01', end='2021-01-01', progress = False)
    meanOfStocks = stocks['Close'].mean(axis = 0)
    print("IBM 2020 average stock value:" + str(meanOfStocks))
    
    print("\nThere are "  + str(len(stocks)) + " rows of stock data.\n")
    variance = 0
    for i in range(len(stocks['Close'])):
        variance += ((stocks['Close'][i]-meanOfStocks) ** 2)/ (len(stocks['Close']) - 1)
        
        
    print("IBM stock variance: {:.2f}".format(variance))
    std = (math.sqrt(variance))
    print("IBM stock standard deviation: {:.2f}\n".format(std))
    
    print("The max stock value {:.2f} was on {:%Y-%m-%d}".format(stocks["Close"].max(), stocks["Close"].idxmax())) 
    print("The min stock value {:.2f} was on {:%Y-%m-%d}".format(stocks["Close"].min(), stocks["Close"].idxmin())) 
    
    
main()


















