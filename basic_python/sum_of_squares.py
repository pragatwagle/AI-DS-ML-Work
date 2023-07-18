# The program calculates the sum of first n numbers and sum of their cubes.
# File: Question_4.py
# Date: 06/09/2021
# Author: Pragat Wagle
# Question 4

def square_each(nums):
    sumOfSqaures = 0
    for i in range(len(nums)) :
        nums[i] = (nums[i] ** 2)
    
def sum_list(nums): 
    sumOfLine = 0
    for i in nums:
        sumOfLine += i
    return sumOfLine
        
    
def to_numbers(str_list):
    for c in range(len(str_list)):
        str_list[c] = float(str_list[c])

def main():
    print("The program prints the sum of squares of each line in a file.")
    filename = input("Enter the name of file with numbers: ")
    print(end = "\n")
    f = open(filename)
    lines = [line.rstrip("\n") for line in f]
    str_list= []
    for line in lines:
        str_list.append(line.split(" "))
    for i in range(len(str_list)):
        to_numbers(str_list[i])
        square_each(str_list[i])
        lineSum = sum_list(str_list[i])
        print("Sum of squares in line", i + 1, "is", lineSum)
    f.close()

main()













