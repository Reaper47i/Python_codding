def array_manu(queries, n):
    out_list = []
    for r in range(n):
        out_list.append(int(0))
    output = 0
    max_elem = 0
    '''for i in range(len(queries)):
        lower_limit = queries[i][0]
        upper_limit = queries[i][1]
        querry = queries[i][2]

        for z in range(n):
            if z >= lower_limit - 1 and z <= upper_limit - 1:
                output = out_list[z] + querry
                out_list[z] = output  this is a old way of computing and takes too much space and time T = O(n^2) '''

    for x, y, z in queries:
        out_list[x:y] += z

    max_elem = max(out_list)

    return max_elem


if __name__ == '__main__':
    #n = int(input())
    n = 10
    no_of_operations = 3  # int(input())

    queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]

    '''for i in range(no_of_operations):
        queries.append(list(map(int, input().rstrip().rsplit())))'''

    #Max = array_manu(queries, n)
    # print(Max)
    print(queries[3])
