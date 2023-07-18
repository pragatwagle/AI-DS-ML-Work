# Program that uses numpy to scores, delete frist row, and replaces missing data with zeros, and prints and then saves the file
# Date: 07/02/2021
# Author: Pragat Wagle

import numpy as np

def main():
    data = np.genfromtxt('Scores_all.csv',delimiter=',')
    date_updated = np.delete(data, 0, axis = 0)
    isNan = np.isnan(date_updated)
    date_updated[isNan]= 0
    scores_int = date_updated.astype(int)
    print(scores_int)
    np.save("scores.npy", date_updated)
        
main()















