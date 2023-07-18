# Program to check if the input numbers are sorted.
# Date: 06/27/2021
# Author: Pragat Wagle

def to_numbers(nums):
    for i in range(len(nums)):
        try:
            num = int(nums[i])
            isNum = True
            if isNum:
                nums[i] = num
        except ValueError:
            return False
    return True            
    
def is_ascend(nums):
    is_asc = False
    for n in range(len(nums)-1):
        if nums[n] <= nums[n+1]:
            is_asc = True
        else:
            is_asc = False
            return is_asc
    return is_asc
  
    
def is_descend(nums):
    is_dsc = False
    for n in range(len(nums)-1):
        if nums[n] >= nums[n+1]:
            is_dsc = True
        else:
            is_dsc = False
            return is_dsc
    return is_dsc
            
def are_same(nums):
    are_sm = False
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[i] == nums[j+1]:
                are_sm = True
            else:
                return           
    return are_sm
           
    
def main():
    print("A program to check if the input numbers are sorted.\n")
    numbers = input("Enter numbers separated by a space: ")
    if not numbers:
        print("Error! No input number.")
        return
    numsSplit = numbers.split(" ")
    nums = to_numbers(numsSplit)
    if nums == False:
        print("Error! The input is not a number!")
        return
    if len(numsSplit) == 1:
        print("You entered a single number.")
        return

    
    
    same = are_same(numsSplit)
    is_asc = is_ascend(numsSplit)
    is_dsc = is_descend(numsSplit)
    
  
    if(same):
        print("The  numbers  are  the  same")
    if(is_asc):
        print("The numbers are in ascending order.")
        return
    if(is_dsc):
        print("The numbers are in descending order.")
        return
    if (is_asc == False) and (is_dsc == False):
        print("The numbers are not sorted.")
        return
    

main()
















