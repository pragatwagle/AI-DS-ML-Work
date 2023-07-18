# The program determines a valid date in a leap year.
# Date: 06/16/2021
# Author: Pragat Wagle

import datetime

def in_date():
    month = input("\nEnter the month: ")
    day = input("\nEnter the day: ")
    year = input("\nEnter year as: ")
    return [month, day, year]
def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
    else:
        return False
def is_month(month):
    month = month.lower().strip()
    if month == "january" or month == "february" or month == "march" or month == "april" or month == "may" or month == "june" or month == "july" or month == "august" or month == "september" or month == "october" or month == "november" or month == "december":
        return True
    else:
        return False
    
def is_day(month, day):
    month = month.lower().strip()
    if (month == "february"):
        if day <= 29 and day > 0:
            return True

    if month == "january" or month == "march" or month == "may" or month == "july" or month == "september"  or month == "november":
       if day <= 31 and day > 0:
           return True
 
    if  month == "april" or month == "june" or month == "august" or month == "october" or month == "december":
        if day <= 30 and day > 0:
            return True
            
    return False
        
                              
        

def main():
    print("The program determines a valid date in a leap year.\n")
    # [month, day, year].    
    inputDate = in_date();
    if(int(inputDate[2]) > 2019) or (int(inputDate[2]) < 1):
        print("Error the year is not a positive integer between 1 and 2019")
        return
    if((is_leap_year(int(inputDate[2])) == False)):
        print("Entered year is not a leap year")
        return
    if((is_month(inputDate[0]) == False)):
        print("Entered month is not a valid month")
        return
    if(is_day(inputDate[0], int(inputDate[1])) == False):
        print("Error! You entered an invalid day in" , inputDate[0])
        return
    else:
        print("You entered a valid date in a leap year!")
        
           
     
         
         
         
        
    
    print(inputDate)

main()















