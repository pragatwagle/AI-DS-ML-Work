# The program calcuates the wind chill.
# File: Question_1.py
# Date: 05/27/2021
# Author: Pragat Wagle
# Question 1

import math 

def main():
    print("The program calcuates the wind chill.\n")
    temp = float(input("Enter the temperature in degrees Fahrenheit: "))
    windSpeed = float(input("\nEnter wind speed in miles per hour: "))
    windChill = 35.74 + (0.6215 * temp) - (35.75 * (math.pow(windSpeed, 0.16))) + (0.4275 * temp * (math.pow(windSpeed, 0.16)))
    print("The wind chill index is", round(windChill,1)) 

main()





