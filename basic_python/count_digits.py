# The program prints the number of digits in each line of a file.
# File: Question_5.py
# Date: 06/09/2021
# Author: Pragat Wagle
# Question 5

def count_digits(line):
    digits = 0
    for c in line:
        if c.isdigit():
            digits += 1
    return digits
def main():
    print("The program prints the number of digits in each line of a file.", end = "\n")
    filename = input("Enter the name of input text file: ")
    file = open(filename)
    lines = [line.strip() for line in file]
    print(end= "\n")
    for line in range(len(lines)):
        digits = count_digits(lines[line])

        print("There are {:2}".format(digits), "digits in line", line + 1)
    
        
    
 
        
main()













