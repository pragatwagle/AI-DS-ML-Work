# The program prints letter X in n lines using character c
# File: Question_2.py
# Date: 06/09/2021
# Author: Pragat Wagle
# Question 2

def print_X(n, c):
    for i in range(0, n):
        indicesOfLeft = n - 1 - i
        for j in range(0, n):
            if(j == indicesOfLeft or j == i):
                print(c, end = "")
            else:
                print(end = " ")
        print(" ")
    
def main():
    num = int(input("Please enter a postive and odd integer: "))
              
    if num < 0 or (num % 2) == 0:
            print("\nProgram quit, a odd postive integer was expected.")
            return
    c = input("Please enter a character c: ")
    print("\n")
    print_X(num, c) 
        
main()













