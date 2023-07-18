# Program that converts kilometers to miles
# File: Question_1.py
# Date: 05/19/2021
# Author: Pragat Wagle
# Question 1

def main():
    print("This program converts kilometers to miles.")
    
    kilometers = float(input("Enter the distance in kilometers: "))
    # body of the program km = eval( ... ) miles = ... print(...)
    factor = 0.62
    miles = kilometers * factor
    print("The distance is {} miles".format(miles))
    
main()