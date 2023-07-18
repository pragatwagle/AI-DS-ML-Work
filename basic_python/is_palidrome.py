# The rogram  that  prompts  the  user  for  a  string,  determines  if  the  string  is  a palindrome,
# File: Question_4.py
# Date: 06/04/2021
# Author: Pragat Wagle
# Question 4

from math import *
import inflect

def main():
    print("The program checks if an input string is a palindrome.\n")
    inputString= input("Enter a string ")
    isPalindrome = True
    
    for c in range(len(inputString)):
        if(inputString[c] != inputString[len(inputString) - (c+1)]):
            isPalindrome = False

    if(isPalindrome):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
        
main()










