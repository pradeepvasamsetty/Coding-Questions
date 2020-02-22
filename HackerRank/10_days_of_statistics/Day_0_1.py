# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

import numpy as np
from scipy import stats

if __name__=="__main__":

    N = int(input()) # Not needed; so overwrite var with next input
    X = list(map(int, input().split()))

    #print(X)

    print(np.mean(X))
    print(np.median(X))
    print(stats.mode(X).mode[0])


    


        

    


        