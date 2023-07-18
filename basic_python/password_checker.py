# The program checks passwords.
# Date: 06/16/2021
# Author: Pragat Wagle

def main():
    #Taking password input
    password = input("Please enter a password: ")
    checkSpecial = False
    
    #ensuring that length is 4 or less
    if(len(password) < 4):
        print("Error: The password has less than 4 characters!")
        return
    #ensuring that length is 8 or less 
    if(len(password) > 8):
        print("Error: The password has more than 8 characters!")
        return
    #checking that first letter is a character 
    if(password[0].isalpha() == False):
        print("Error: The first character is not a letter")
        return
    #check for one number between 1-9
    if(any(c.isdigit() for c in password) == False):
        checkSpecial = False
        print("Error: The password contains no number between 0 and 9!")
        return
    #checking for one character from [$#@] 
    for c in password:
        if c=="$" or c=="#" or c=="@":
            checkSpecial = True
    if (checkSpecial == False):
            print("Error: The password does not have at least one character from [$#@]!")
            return
        
    print("You entered a valid password")

main()

















