#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    rPos = rNeg = 0.0
    rZero = 0
    for x in range(len(arr)):
        if arr[x] == 0:
            rZero += 1
        elif arr[x] >= 1:
            rPos += 1
        else:
            rNeg += 1

    rZero = rZero/len(arr)
    rPos = rPos/len(arr)
    rNeg = rNeg/len(arr)

    return rPos, rNeg, rZero


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    newArr = []
    newArr = (plusMinus(arr))
    for x in range(len(newArr)):
        print(newArr[x])
