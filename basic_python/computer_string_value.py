# The program that calculates the numeric value of a single name (in lower case letters) provided as input.
# File: Question_3.py
# Date: 06/04/2021
# Author: Pragat Wagle
# Question 3

from math import *
import inflect

def main():
    print("The program computes the value of a string.\n")
    inputString= input("Enter any name in lower case: ")
    alphabet = { 'a':1 , 'b':2 , 'c':3 , 'd':4 , 'e':5, 'f':6 , 'g':7, 'h':8, 'i':9 , 'j':10 , 'k':11 , 'l':12, 'm':13, 'n':14 , 'o':15, 'p':16 ,'q':17 , 'r':18 , 's':19, 't':20, 'u':21, 'v':22 , 'w':23 , 'x':24, 'y':25 , 'z':26}  
    alphabetSum = 0
    for c in inputString:
        alphabetSum += alphabet[c]

    print("The numeric value of the name is", alphabetSum)
        
main()









