

def move_spiral(arr,n,m):
    res = []
    start = 0
    stop = n-1
    for i in range(n):
        start = i
        stop = m
        while(start<stop):
            temp = arr[start][stop]
            if start == m-1:
                start = 1
                stop = 

            res.append(temp)



if __name__ == "__main__":
    n = 4
    m = 4
    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    res = move_spiral(arr,n,m)
    print(res)