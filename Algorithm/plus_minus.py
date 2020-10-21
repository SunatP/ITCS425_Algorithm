#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    sum = 0
    pos = 0
    neg = 0
    zero = 0
    zero_total=0
    pos_total = 0
    neg_total = 0
    total = len(arr)
    for i in range(len(arr)):
        if arr[i] > 0 :
            pos+=1
            sum = abs(pos/total)
        elif arr[i] < 0:
            neg+=1
            sum = abs(neg/total)
        else:
            zero+=1
            sum = abs(zero/total)
    
    zero_total = "{:.6f}".format(abs(zero/total))
    pos_total = "{:.6f}".format(abs(pos/total))
    neg_total = "{:.6f}".format(abs(neg/total))
    print(pos_total)
    print(neg_total)
    print(zero_total)
    
    # formatted_float = "{:.2f}".format(a_float)

if __name__ == '__main__':
    n = float(input())

    arr = list(map(float, input().rstrip().split()))

    plusMinus(arr)
