# Program that uses NumPy to calculate and print average of each assignment group.
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
    print("Program to calculate assignment group averages.")
    data = np.load("scores.npy")
    average_hw = averageColumn(data[1:,1:7])
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
    hwtotal = 0
    labtotal = 0
    quiztotal = 0
    projecttotal = 0
    midtermtotal = 0
    midterm2total = 0
    avgs = []
    for i in range(len(rounded_hw)):
        hwtotal += rounded_hw[i]
    hwavg = hwtotal/len(rounded_hw)
    avgs.append(hwavg)
    for i in range(len(rounded_labs)):
        labtotal += rounded_labs[i]
    labavg= labtotal/len(rounded_labs)
    avgs.append(labavg)
    for i in range(len(rounded_quizzes)):
        quiztotal += rounded_quizzes[i]
    quizavg = quiztotal/len(rounded_quizzes)
    avgs.append(quizavg)

    for i in range(len(rounded_fp)):
        projecttotal += rounded_fp[i]
    projavgs = projecttotal/len(rounded_fp)
    avgs.append(projavgs)

    for i in range(len(rounded_midterm)):
        midtermtotal += rounded_midterm[i]
    midtermavg = midtermtotal/len(rounded_midterm)
    avgs.append(midtermavg)

    for i in range(len(rounded_midterm2)):
        midterm2total += rounded_midterm2[i]
    midterm2mavg = midterm2total/len(rounded_midterm2)
    avgs.append(midterm2mavg)
    rounded_avgs= np.around(avgs, decimals = 1)
    print("Homework average:\t" + str(rounded_avgs[0]))
    print("Lab average:\t\t" + str(rounded_avgs[1]))
    print("Quiz average:\t\t" + str(rounded_avgs[2]))
    print("Project average:\t" + str(rounded_avgs[3]))
    print("Midterm 1 average:\t" + str(rounded_avgs[4]))
    print("Midterm 2 average:\t" +  str(rounded_avgs[5]))

   

main()

















