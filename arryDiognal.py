
import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    sumD1 = sumD2 = diff = 0
    for x in range(len(arr)):
        sumD1 += arr[x][x]
        sumD2 += arr[x][len(arr)-1-x]

    if sumD1 > sumD2:
        diff = sumD1-sumD2
    else:
        diff = sumD2-sumD1

    return diff


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
