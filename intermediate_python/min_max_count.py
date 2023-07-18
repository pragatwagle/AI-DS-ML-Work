# Program prints min, max, and count of positive and negative numbers
# File: Question_1.py
# Date: 06/16/2021
# Author: Pragat Wagle
# Question 1

def main():
    numbers = []
    isNum = False
    print("Program prints min, max, and count of positive and negative numbers")
    try:
        firstNum = input("Enter a number: ")
        firstNum = int(firstNum)
        isNum = True
        if isNum:
            numbers.append(int(firstNum))
    except ValueError:
        firstNum = input("Error! Please enter a valid number:")
        isNum = True
        if isNum:
            numbers.append(int(firstNum))
    minNum = numbers[0]
    maxNum = numbers[0]
    countPos = 0
    countNeg = 0
    while firstNum != "":
        try:
            firstNum = input("Enter the next number: ")
            isNum = True
            if isNum:
                numbers.append(int(firstNum))
        except ValueError:
            isNum = False

    for i in range(len(numbers)) :
        if maxNum > numbers[i]:
            maxNum = maxNum
        else:
            maxNum = numbers[i]
    for i in range(len(numbers)) :
        if minNum < numbers[i]:
            minNum = minNum
        else:
            minNum = numbers[i]
    for i in range(len(numbers)) :
        if numbers[i] > 0:
            countPos += 1
    for i in range(len(numbers)):
        if numbers[i] < 0:
            countNeg += 1
            
    print("\nYou entered", len(numbers), "numbers.")
    print("The smallest number is ", float(minNum))
    print("The largest number is ", float(maxNum))
    print("There are", countPos, "postive and", countNeg, "negative number(s)")
        
        

    

main()















