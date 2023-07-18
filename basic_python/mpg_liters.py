# Program that converts kilometers to miles # File: question1.py
# File: Question_2.py
# Date: 05/19/2021
# Author: Pragat Wagle
# Question 2
def main():
    print("The program converts mileage to liters per 100 km.\n")
    
    mileage = int(input("Please enter mileage (miles per gallon): "))
    # body of the program km = eval( ... ) miles = ... print(...)
    # mile to km factor 
    kmToMileFactor = 1.6
    # gal to liter factor
    galToLiterFactor = 3.785
    kmFactor = 0.62137119
    kilometersFromMpg = mileage * 1.6
    fractionOf100 = 100/kilometersFromMpg
    galPerMile = galToLiterFactor * fractionOf100
    
    
    
    print("\nVehicle economy is {} miles per gallon.".format(mileage))
    print("Vehicle consumption {} liters per 100 km.".format(galPerMile))
    
    
main()
