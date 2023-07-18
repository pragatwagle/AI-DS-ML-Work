# Program that uses NumPy to calculate and print average score for each assignment
# Date: 07/02/2021
# Author: Pragat Wagle

import numpy as np

def averageColumn(df_array):
    average = []
    for col in range(df_array.shape[1]):
        data  = df_array[:, col]
        sum_df = np.sum(data, dtype = np.float)
        avg = sum_df/44
        average.append(avg)
        
    return average 

def main():
    data = np.load("scores.npy")
    average_hw = averageColumn(data[1:,1:7])
    print(average_hw)
    average_labs = averageColumn(data[1:, 7:18])
    average_fp= averageColumn(data[1:, 18:19])
    average_midterm = averageColumn(data[1:, 19:20])
    average_quizzes = averageColumn(data[1:, 20:29])
    average_midterm2 = averageColumn(data[1:, 29:30])
    rounded_hw = np.around(average_hw, decimals = 1)
    rounded_labs = np.around(average_labs, decimals = 1)
    rounded_fp = np.around(average_fp, decimals = 1)
    rounded_midterm = np.around(average_midterm, decimals = 1)
    rounded_quizzes = np.around(average_quizzes, decimals = 1)
    rounded_midterm2 = np.around(average_midterm2, decimals = 1)

    for i in range(len(rounded_hw)):
        print("Homework " + str(i) + " average: " + str (rounded_hw[i]))
    for i in range(len(rounded_labs)):
        print("Lab\t " + str(i) + " average: " + str (rounded_labs[i]))
    for i in range(len(rounded_quizzes)):
        print("Quiz\t" +" " + str(i) + " average: " + str (rounded_quizzes[i]))
    for i in range(len(rounded_fp)):
        print("\nFinal Proect avg: " + str (rounded_fp[i]))
    for i in range(len(rounded_midterm)):
        print("Midterm 1 " + "average: " + str (rounded_midterm[i]))
    for i in range(len(rounded_midterm2)):
        print("Midterm 2 "  + " average: " + str (rounded_midterm2[i]))
    

main()


















