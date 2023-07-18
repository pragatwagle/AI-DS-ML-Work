# The program counts number of words in an input file.
# File: Question_5.py
# Date: 06/04/2021
# Author: Pragat Wagle
# Question 5

def main():
    
    print("The program counts number of words in an input file.\n")
    fileName = input("Enter a filename: ")
    fileText = open(fileName, 'r')
    words = []
    for line in fileText:
        words += line.split()
      
    
    print("There are" ,len(words), "words in the file.")
        
main()











