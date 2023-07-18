# The program takes a positive integer number from the user and prints the number in words.
# File: Question_2.py
# Date: 06/04/2021
# Author: Pragat Wagle
# Question 2

from math import *
import inflect

def main():
    print("The program spells the input number.\n")
    inputString= input("Please enter a number: ")
    integers = [int(c) for c in inputString]
    integersAsString = ""
  
    for i in range(len(integers)):
        p = inflect.engine()
        integersAsString += p.number_to_words(inputString[i]) + " "

    print("You typed a number: ", inputString)
    print("The number in words: ", integersAsString)
        
main()








