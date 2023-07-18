# Program that uses NumPy to read file “scores.npy” and create a NumPy array “score_headings” with columns
# Date: 07/02/2021
# Author: Pragat Wagle


import numpy as np
import warnings

def main():
    warnings.filterwarnings("ignore")
    columns = ('ID numbers', 'Weighted scores for the homework assignment', 'Weighted scores for the labs', 'Weighted final project scores','Weighted midterm 1 scores', 'Weighted scores for the quizzes', 'Weighted midterm 2 scores')
    data = np.load("scores.npy")
    id_nums = (data[1:, 0:1])
    id_reshaped = np.reshape(id_nums, (44))
    id_converted = id_reshaped.astype(np.float)
    hw = (data[1:, 1:7]).sum(axis = 1)
    hw_weighted = (hw/600) * .2
    hw_converted = hw_weighted.astype(np.float)
    hw_converted = hw_converted * 100
    labs = (data[1:, 7:18]).sum(axis = 1)
    labs_weighted = (labs/1100) * .3
    labs_reshaped = np.reshape(labs_weighted, (44))
    labs_converted = labs_reshaped.astype(np.float)
    labs_converted = labs_converted * 100


    fp = (data[1:, 18:19])
    fp_weighted = (fp/100) * .1
    fp_reshaped = np.reshape(fp_weighted, (44))
    fp_converted = fp_reshaped.astype(np.float)
    fp_converted = fp_converted * 100


    midterm = (data[1:, 19:20]).sum(axis = 1)
    midterm_weighted = (midterm/100) * .1
    midterm_reshaped = np.reshape(midterm_weighted, (44))
    m_converted = midterm_reshaped.astype(np.float)
    m_converted = m_converted * 100



    quizzes = (data[1:, 20:29]).sum(axis = 1)
    quizzes_weighted = (quizzes/90) * .15
    quizzes_reshaped = np.reshape(quizzes_weighted, (44))
    q_converted = quizzes_reshaped.astype(np.float)
    q_converted = q_converted * 100

 
    midterm2 = (data[1:, 29:]).sum(axis = 1)
    midterm2_weighted = (midterm2/100) * .15
    midterm2_reshaped = np.reshape(midterm2_weighted, (44))
    
    m2_converted = midterm2_reshaped.astype(np.float)
    m2_converted = m2_converted * 100

    np.set_printoptions(suppress=True)
    scores_array =  np.stack([id_converted, hw_converted,labs_converted, fp_converted, m_converted, q_converted, m2_converted ], axis=1) 
    rounded_scores = np.around(scores_array, decimals = 1)
    print(rounded_scores)
    np.save("score_headings", rounded_scores)



    

main()
















