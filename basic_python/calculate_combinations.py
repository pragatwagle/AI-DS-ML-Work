# The program calculates the number of combinations of n objects taken r at a time.
# File: Question_3.py
# Date: 06/09/2021
# Author: Pragat Wagle
# Question 3

def factorial(m):
    if m < 2:
        return 1
    return m * factorial(m-1)


def main():
    print("Calculates the number of combinations of n objects taken r at a time.\n") 
    n = int(input("Enter a positive integer n: "))
    r = int(input("Enter a positive integer r: "))
    if n < r:
        print("Error! Number n is less than r!")
        return
    numberOfCombinations = (factorial(n))/((factorial(r) * factorial(n-r)))    
    print("Number of combinations C( 5 , 3 )", numberOfCombinations)
    
 
        
main()













