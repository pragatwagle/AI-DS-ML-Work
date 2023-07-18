# Program that calculates relative standard deviation for eight Dow Jones companies. 
# Date: 07/11/2021
# Author: Pragat Wagle

import numpy as np
import yfinance as yf
import math
from math import sqrt

def rel_std(data):
    stocksClose = data["Close"].mean(axis=0)
    meanStocksClose = stocksClose.mean(axis=0)
    companyNames = {'BA':0, 'KO':0,'XOM':0,'GE':0, 'JPM':0,'NKE':0, 'PFE':0, 'VZ': 0}
    related_std = {}
    for key, value in companyNames.items():
        variance = 0
        for i in range(len(data['Close'])):
            variance += ((data['Close'][key][i]-stocksClose[key]) ** 2)/ (len(data['Close'][key]) - 1)
            std = (math.sqrt(variance))
            rel_std = (std)/(stocksClose[key]) * 100
            companyNames[key] = str(round(rel_std, 2))
    return companyNames
        
        
      



def main():
    print("Program that calculates relative standard deviation for eight Dow Jones companies.\n")
    stocks = yf.download('ba ko xom ge jpm nke pfe vz', start = '2020-01-01', end='2021-01-01', progress = False)   
    stocksClose = stocks["Close"].mean(axis=0)
    meanStocksClose = stocksClose.mean(axis=0)
    relativeStd = rel_std(stocks)
    print("Company               Relative std deviation ")
    print("--------------------------------------------")
        
    companyNames = {"BA":"Boeing", "KO":"Coca-Cola","XOM":"Coca Cola","GE":"General Electric", "JPM":"JP Morgan","NKE":"Nike",
                    "PFE":"Pfeizer", "VZ":"Verizon"}
    
    for key in relativeStd:
        line_new = '{0:20}  {1}'.format(companyNames[key], relativeStd[key])
        print(line_new)

        
        
  
main()





















