#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 08:59:59 2021

@author: pragatwagle
"""

#2

# 2.1
def circleArea(r):
    area = 2 * 3.14 * r
    print(area)

circleArea(2)

# 2.2
def kilometersToMiles(km):
    mile = km * .62
    print(mile)
    
kilometersToMiles(600)

# 2.3
def squareArea(side):
    area = side * side * side
    print(area)
    
squareArea(12)

# 3 
def firstFiveSquares():
    for i in range(1, 6, 1):
        square = i ** 2  
        print(square)
        
firstFiveSquares()

def firstTenReverse():
    for i in reversed(range(2, 21, 2)):
        print(i)

firstTenReverse()

        
        






