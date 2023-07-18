# The program prints the count of numbers divisible by 7.
# File: Question_3_2.py
# Date: 05/27/2021
# Author: Pragat Wagle
# Question 3.2

from math import *

def main():
    print("The program prints the numbers divisible by 7.\n")
    positiveInteger = int(input("Enter a positive integer: "))
    countDivisibleBy7 = 0
    for i in range(1, positiveInteger + 1):
        if(i % 7 == 0):
            countDivisibleBy7 += 1
    if(countDivisibleBy7==1):
        print("There is", countDivisibleBy7, "number between 1 and", positiveInteger,"that is divisible by 7:")
    else:
        print("There are", countDivisibleBy7, "numbers between 1 and", positiveInteger,"that are divisible by 7:")

main()






