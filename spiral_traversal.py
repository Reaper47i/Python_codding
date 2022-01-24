'''
for spiral movement first we map all the 
edges of the matrix X[m*n]
top = 0, bottom = n-1
left = 0 , right = m-1

lets take var dir = 0 which lets us 
know which direction to take and then 
we append when condition comes true

loop : top<bottom and left<right:
        if dir = 0:
            loop from left to right
                top+=1
        if dir = 1:
            k = 1
            loop from top to bottom:
                arr[i+k]][j]
            right-=1
        if dir = 2:
            k = m-2
            loop from right - left:
                arr[i-k][j]
            bottom-=1
            
        if dir = 3:
            k = m-2
            loop from bottom to top
            left+=1
        
        also dir = (dir+1)%4


'''




def move_spiral(arr,n,m):
    _dir = 0
    top = 0
    bottom = n
    left = 0
    right = m
    res = []
    while(left<right and top<bottom):
        if _dir == 0:
            for i in range(left,right):
                res.append(arr[top][i])
            
            top+=1
        if _dir == 1:
            for i in range(top,bottom):
                res.append(arr[i][right-1])
            
            right-=1
        if _dir == 2:
            for i in range(right-1,left-1,-1):
                res.append(arr[bottom-1][i])
            
            bottom-=1
            
        if _dir == 3:
            for i in range(bottom-1,top-1,-1):
                res.append(arr[i][left])
            
            left+=1
        
        _dir = (_dir+1)%4

        

    
    return res


if __name__ == "__main__":
    n = 4
    m = 4
    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    res = move_spiral(arr,n,m)
    print(*res)