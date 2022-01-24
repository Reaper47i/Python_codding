def minimum_bribes(ls):
    bribes = 0
    size = len(ls)
    for i,j in enumerate(ls):
        if j-1-i > 2:
            return("Too Chaotic")
        else:
            for k in range(max(j-2,0),i):
                if(ls[k]>j):
                    bribes+=1
            
    
    return bribes



if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input().strip())
        q = list(map(int, input().rstrip().split()))
        print(minimum_bribes(q))
    
        

    


'''
1 2 3 4 5 6
1 2 3 4 6 5
1 2 3 6 4 5
1 2 6 3 4 5
1 2 6 4 3 5
2 1 6 4 3 5

6-1 + 5-3 + 3-6 + 2-1 + 1-2 = 

2 1 6 4 3 5
'''