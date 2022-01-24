


def tripletSum(arr,n,k):
    arr.sort() 
    for i in range(n-2):
        l = i+1
        r = n-1
        while(l<r):
            _sum = arr[i]+arr[l]+arr[r]

            if _sum == k:
                return True
            elif _sum < k:
                l+=1
            else:
                r-=1
    
        return False

if __name__ == "__main__":
    n = 6
    x = 13
    a = [1,4,45,6,10,8]
    res = tripletSum(a,n,x)
    if(res):
        print(1)
    else:
        print(0)



'''
combinations possible:-
1 4 45 6 10 8
1 4 45 , 1 4 6 , 1 4 10, 1 4 8
1 


'''

