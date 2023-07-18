# The program calculates the length of a ladder
# File: Question_1.py
# Date: 05/27/2021
# Author: Pragat Wagle
# Question 2

from math import *

def main():
    print("The program calculates the length of a ladder.\n")
    height = float(input("Enter the height in feet: "))
    angle = float(input("\nEnter the angle in degrees: "))
    rads = ((pi / 180) * angle)
    length = (height / sin(rads))
    print("The length of the ladder is ", round(length,2), "feet") 

main()




