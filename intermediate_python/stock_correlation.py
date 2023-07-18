# Program calculates sample correlation between Boeing and Coca Cola closing stock values in 2020
# Date: 07/11/2021
# Author: Pragat Wagle

import numpy as np
import yfinance as yf
import math
from math import sqrt

def correl(stock1, stock2):
    stock1meanforCalculation = stock1["Close"].mean(axis=0)
    stock1mean = str(round(stock1meanforCalculation, 2))

    print("Average Boeing stock value:{}".format(str(stock1mean).rjust(25)))
    numerator1 = 0
    for i in range(len(stock1['Close'])):
        numerator1 += ((stock1['Close'][i]-stock1meanforCalculation) ** 2)
    stdstock1 = (math.sqrt(numerator1/(len(stock1['Close']) - 1)))
    stdrounded = str(round(stdstock1, 2))

    print("Std deviation of Boing stock:" + stdrounded.rjust(25))

    stock2meanforCalculation = stock2["Close"].mean(axis=0)
    stock2mean = str(round(stock2meanforCalculation, 2))
    
    print("\nAverage Coca Cola stock value:{}".format(str(stock2mean).rjust(23)))
    numerator2 = 0
    for i in range(len(stock2['Close'])):
        numerator2 += ((stock2['Close'][i]-stock2meanforCalculation) ** 2)
    
    stdstock2 = (math.sqrt(numerator2/(len(stock2['Close']) - 1)))
    stock2rounded = str(round(stdstock2, 2))
    print("Std deviation of Coca Cola stock:" + stock2rounded.rjust(21))

    
    cov = 0
    for i in range(len(stock2['Close'])):
        differenceInStock2 = (stock2['Close'][i]-stock2meanforCalculation)
        differenceInStock1 = (stock1['Close'][i]-stock1meanforCalculation)
        cov += (differenceInStock2 * differenceInStock1)/(len(stock2['Close']-1))

    correlation = (cov/(stdstock1 * stdstock2))
    correlationrounded = str(round(correlation, 2))

    print("\nCorrelation between BA and KO:" + correlationrounded.rjust(23))

def main():
    print("Program calculates sample correlation between Boeing and Coca Cola closing stock values in 2020.\n")
    boeing = yf.download('ba', start = '2020-01-01', end='2021-01-01', progress = False)   
    cocacola = yf.download('ko', start = '2020-01-01', end='2021-01-01', progress = False)   

    relativeStd = correl(boeing, cocacola)
       
        
        
  
main()




















