# The program calculates the body mass index.
# Date: 06/16/2021
# Author: Pragat Wagle

def body_mass_index(inches, lbs):
    kg = lbs * .4536
    meters = inches * 0.0254
    bmi = kg / (meters**2)
    return bmi

def main():
    print("Program calculates the body mass index.\n")
    
    try:
        height = input("\nEnter your height in inches: ")
        height = float(height)

    except ValueError:
        print("Error! You entered a string that is not a number!")
        return
        
    if (height < 0):
        print("Error! You entered a negative number!")
        return
    try:
        weight = input("Enter your weight in pounds: ")
        weight = float(weight)
        
    except ValueError:
        print("Error! You entered a string that is not a number!")
        return
    
    if (weight < 0):
        print("Error! You entered a negative number!")
        return
    else:
        bmi  = body_mass_index(height, weight)
        if(bmi < 19):
            print("Your BMI is", bmi , "you are below the healthy range!")
            
        elif(bmi >= 19) and (bmi <= 25):
            print("Your BMI is", bmi , "you are within the healthy range!")
            
        else:
            print("Your BMI is", bmi , "you are above the healthy range!") 

main()














