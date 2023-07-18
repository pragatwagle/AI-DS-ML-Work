# The program calculates the sum of first n numbers and sum of their cubes.
# File: Question_1.py
# Date: 06/09/2021
# Author: Pragat Wagle
# Question 1

def sum_n(n):
    sumOfInts = 0
    for i in range(n + 1):
        sumOfInts += i
    return sumOfInts
    
def sum_cubes(n):
    sumOfIntsCubed = 0
    for i in range(n + 1):
        value = i ** 3
        sumOfIntsCubed += value
    return sumOfIntsCubed

def main():
    print("The program calculates the sum of first n numbers and sum of their cubes.\n") 
    number = eval(input("Please enter a positive integer: "))
    if number <= 0:
        print("You entered a number, which is not a positive integer.")
        return
    sumOfInts = sum_n(number)
    sumCubed = sum_cubes(number)
    
    print("The sum of first 5 positive integers is:", sumOfInts)
    print("sum of cubes of first 5 positive integers is:", sumCubed)
    
 
        
main()












