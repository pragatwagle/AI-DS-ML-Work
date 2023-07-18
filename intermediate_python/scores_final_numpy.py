# Program that uses NumPy to read file “scores.npy” and create a NumPy array “score_headings” with columns
# Date: 07/02/2021
# Author: Pragat Wagle


import numpy as np

def to_letter_grade(score):
    if(score==100):
        return "A+"
    if(score>=93 and score<100):
        return "A"
    if(score<93 and score>=90):
        return "A-"
    if(score<90 and score>=87):
        return "B+"
    if(score<87 and score>=83):
        return "B"
    if(score<83 and score>=80):
        return "B-"
    if(score<80 and score>=77):
        return "C+"
    if(score<77 and score>=73):
        return "C"
    if(score<73 and score>=70):
        return "C-"
    if(score<70 and score>=67):
        return "D+"
    if(score<67 and score>=63):
        return "D"
    if(score<63 and score>=60):
        return "D-"
    if(score<60):
        return "F"
    
    
def main():
    data  = np.load("score_headings.npy")
    ids = (data[0:,0:1])
    ids_reshaped = np.reshape(ids, (44)) 
    scores = (data[0:,1:7]).sum(axis=1)
    grades = []
    for score in scores:
        grade = to_letter_grade(score)
        grades.append(grade)
    np_grades = np.array(grades)
    fxn = np.vectorize(to_letter_grade)
   
    final_scores= fxn(scores)
    string_grades = final_scores.astype(str)
    rounded_scores = np.around(scores, decimals = 1)
    scores_arr = np.stack([ids_reshaped, rounded_scores, string_grades], axis = 1)
    print(scores_arr)

main()

















