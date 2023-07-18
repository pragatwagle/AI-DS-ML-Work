# The program calculates the letter grade from a total score.
# Date: 06/16/2021
# Author: Pragat Wagle

def letter_grade(n):
    grade = ""
    if (n >= 93) and (n <= 100):
        grade = "A"
    if (n >= 90) and (n <= 92.99):
        grade = "A-"
    if (n >= 86) and (n <= 89.99):
        grade = "B+"
    if (n >= 83) and (n <= 85.99):
        grade = "B"
    if (n >= 80) and (n <= 82.99):
        grade = "B-"
    if (n >= 76) and (n <= 79.99):
        grade = "C+"
    if (n >= 73) and (n <= 75.99):
        grade = "C"
    if (n >= 70) and (n <= 72.99):
        grade = "C-"
    if (n >= 66) and (n <= 69.99):
        grade = "D+"
    if (n >= 60) and (n <= 65.99):
        grade = "D"
    if (n >= 0) and (n <= 65.99):
        grade = "F"
    return grade
    
    
def main():
    print("Program calculates the letter grade from a total score.")
    totalScore = input("Enter your total score: ")
    try:
        num = float(totalScore)
        
    except ValueError:
        print("Error! You entered a string that is not a number!")
        return
    if (num < 0) or (num > 100):
        print("Error! The total score must be between 0 and 100.")
    else:
        letterGrade  = letter_grade(num)
        print("Your letter grade is", letterGrade) 

main()













