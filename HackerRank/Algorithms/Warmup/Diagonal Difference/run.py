#!/bin/python3

# https://www.hackerrank.com/challenges/diagonal-difference/problem

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    """ Returns absolute difference between the sums of its diagonals. """

    diag = [arr[i][i]for i in range(0,len(arr))]
    diag_counter = [arr[i][~i]for i in range(0,len(arr))]

    return abs(sum(diag) - sum(diag_counter))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
