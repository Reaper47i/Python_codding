def minMax(arr):
    minAr = arr.copy()
    maxAr = arr.copy()
    maxSum = minSum = 0
    maxAr.pop(maxAr.index(min(maxAr)))
    for i in range(len(maxAr)):
        maxSum += maxAr[i]

    minAr.pop(minAr.index(max(minAr)))
    for j in range(0, len(minAr)):
        minSum += minAr[j]

    return maxSum, minSum


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().rsplit()))

    print(minMax(arr), end="")
