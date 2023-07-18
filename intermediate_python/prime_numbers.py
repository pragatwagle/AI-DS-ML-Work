# The program prints prime numbers in a range.
# Date: 06/27/2021
# Author: Pragat Wagle

def is_prime(n):
    is_prime = True
    for i in range(10):
        if i != n and i != 0 and i != 1 and i<n:
            if n % i == 0:
                is_prime = False
    
    return is_prime
   

def print_prime(lower_limit, upper_limit):
   
    primes = []
    for i in range(lower_limit, upper_limit + 1):
        if(is_prime(i)):
            primes.append(i)
    print("\nThe sequence of prime numbers in the given interval")
    for i in primes:
        print(i)
        

def main():
    print("The program prints prime numbers in a range.\n")
    
    try:
        lowerLimit = int(input("Enter the lower limit of the range: "))
    except ValueError: 
        print("Error! You entered a non-integer!")
    if(lowerLimit <=1):
        print("Invalid input: Lower limit should be a positive integer, greater than 1")
        return
    try:
        upperLimit = int(input("\nEnter the upper limit of the range: "))
    except ValueError: 
        print("Error! You entered a non-integer!")
        return
    if(upperLimit <=2):
        print("Invalid input: Upper limit should be a positive integer, greater than 2")
        return
    if(lowerLimit>upperLimit):
        print("Invalid input: Upper limit is less than lower limit.")
        return
    
    primes = print_prime(lowerLimit , upperLimit)
    
    
main()


















