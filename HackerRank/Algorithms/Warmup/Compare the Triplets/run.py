#!/bin/python3

# https://www.hackerrank.com/challenges/compare-the-triplets/problem

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    """ Returns score for Alice & Bob by comparing the triplets. """

    score_a = 0
    score_b = 0

    for ele_a,ele_b in zip(a, b):
        if ele_a > ele_b:
            score_a+=1
        elif ele_a < ele_b:
            score_b+=1
        else:
            pass
    
    return [score_a,score_b]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
