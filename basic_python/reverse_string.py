# The program that takes an input string from the user and prints the string in a reverse order.
# File: Question_1.py
# Date: 06/04/2021
# Author: Pragat Wagle
# Question 1

from math import *

def main():
    print("The program prints a string in a reverse order.\n")
    inputString = input("Please enter a string: ")
    reversedString = ""
    for i in range(len(inputString)):
        reversedString += inputString[len(inputString)-(i+1)]

    print("\nYou typed a string: ", inputString)
    print("The string in the reverse order: ", reversedString)

main()










