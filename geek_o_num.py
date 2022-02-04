def gOn(a,b,c,n):
    if n == 0:
        return a
    if n == 1:
        return b
    if n == 2:
        return c

    else:
        return gOn(a,b,c,n-3) + gOn(a,b,c,n-2) + gOn(a,b,c,n-1)
    

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        A,B,C,N = [int(x) for x in input().split()]
        print(gOn(A,B,C,N-1))