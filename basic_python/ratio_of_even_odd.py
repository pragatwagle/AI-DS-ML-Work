# The program  calculates  and  prints  the  ratio  of  the sum  of  even numbers to the sum of all the numbers in the range
# File: Question_5.py
# Date: 05/27/2021
# Author: Pragat Wagle
# Question 5

from math import *

def main():
    start = int(input("Enter start number of a range: "))
    end = int(input("\nnter ending number of a range: "))
    evenSum = 0
    totalSum = 0
    for i in range(start, end + 1):
        if(i % 2 == 0):
            evenSum += i
            totalSum += i
        else:
            totalSum += i
    ratio = evenSum/totalSum
    print("Ratio of sum of even numbers to sum of all numbers in the range is", round(ratio, 3))
   

main()








