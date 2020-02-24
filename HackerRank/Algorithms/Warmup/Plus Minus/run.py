#!/bin/python3

# https://www.hackerrank.com/challenges/plus-minus/problem

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    """ Fractions of its elements that are positive, negative, and are zeros. """

    positive = 0
    negative = 0
    zeros = 0

    for ele in arr:
        if ele > 0:
            positive+=1
        elif ele < 0:
            negative+=1
        else:
            zeros+=1
    
    print(positive/n)
    print(negative/n)
    print(zeros/n)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
