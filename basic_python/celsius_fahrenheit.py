# Print a table of Celsius temperatures and the Fahrenheit
# File: Question_3.py
# Date: 05/19/2021
# Author: Pragat Wagle
# Question 3

def getfahrenheit(celsius):
    fahrenheit= (9/5) * celsius+ 32
    return fahrenheit

def main():
      
    print("Conversion table from Celsius to Fahrenheit\n")
    
    print("Celsius  Fahrenheit")
    print("------------------")
    for i in range(0,11):
        celsius = 10 * i
        fahrenheit = getfahrenheit(celsius)
        print("{}".format(celsius)+"\t"+ "{}".format(fahrenheit))
    
main()

