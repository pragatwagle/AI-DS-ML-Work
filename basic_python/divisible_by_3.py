# The program prints the numbers divisible by 3.
# File: Question_3_1.py
# Date: 05/27/2021
# Author: Pragat Wagle
# Question 3.1

from math import *

def main():
    print("The program prints the numbers divisible by 3.\n")
    positiveInteger = int(input("Enter a positive integer: "))
    if(positiveInteger>1):
        print("Numbers between 1 and", positiveInteger,"divisible by 3 are:")
    else:
        print("The Number between 1 and", positiveInteger,"divisible by 3 is:")
    for i in range(1, positiveInteger + 1):
        if(i % 3 == 0):
            print(i)

main()





