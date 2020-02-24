#!/bin/python3

# https://www.hackerrank.com/challenges/mini-max-sum/problem

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    """ Returns the minimum and maximum values that can be calculated by summing exactly four of the five integers. """

    arr.sort()
    print(sum(arr[0:4]),sum(arr[1:5]))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
