
def compareTriplets(a, b):
    ptA = 0
    ptB = 0
    null = 0
    for x in range(3):
        if a[x] == b[x]:
            null += 1
        elif a[x] > b[x]:
            ptA += 1
        else:
            ptB += 1

    out = [ptA, ptB]
    return out


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)
