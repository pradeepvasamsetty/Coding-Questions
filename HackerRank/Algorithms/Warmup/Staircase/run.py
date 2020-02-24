#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    """ Prints staircase of size n. """

    for step in range(1,n+1):
        print(str('#'*step).rjust(n))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
