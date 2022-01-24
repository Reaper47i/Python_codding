def dynamicArray(n, queries):
    seq = [[] for _ in range(n)]
    lastAns = 0
    result = []

    for q, x, y in queries:
        if q == 1:
            idx = (x ^ lastAns) % n
            seq[idx].append(y)
        else:
            idx = (x ^ lastAns) % n
            v = y % len(seq[idx])
            lastAns = seq[idx][v]
            result.append(lastAns)

    return result


n = input("Enter Number Of Cases: ")
q = input("Enter Queries: ")

finalResult = dynamicArray(n, q)

print(finalResult)
