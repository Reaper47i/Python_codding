def querry(strings, querry_list):
    result = []
    count = 0
    #string_list = list(strings)
    for querry in querry_list:
        if querry in strings:
            count = strings[querry]
            result.append(count)
        else:
            count = 0
            result.append(count)
    return result

    '''count = 0
    result = []
    for querry in range(len(querry_list)):
        for ele in range(len(list)):
            if querry_list[querry] == list[ele]:
                count += 1
            else:
                count += 0

        result.append(count)

        count = 0
    return result
    '''


if __name__ == '__main__':
    S = {}
    n = int(input())

    for i in range(n):
        data = input()
        if data in S:
            count += 1
            S[data] = count
        else:
            count = 1
            S[data] = count

    print(S)

    Q = []
    q = int(input())

    for j in range(q):
        Q.append(input())

    res = querry(S, Q)
    print(res)
