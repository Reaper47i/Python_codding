'''
if condition a[i]<=a[j] and i<=j
find j-i

'''


def max_index(arr,n):
    # h_arr = dict() ---------------------------------->> this is basic method of doing 
    # diff = 0                                            time comp = O(N^2)
    # for i in range(n):                                   Space comp = O(N)
    #     h_arr[arr[i]] = i

    # for j in range(n-1):
    #     for k in range(j+1,n):
    #         if arr[j]<=arr[k]: 
    #             diff = max(diff,k-j)


    # can be done in T.C -> o(n) and S.C -> o(n)
    
    diff = 0

    i = 1
    j = n-2
    
    # if arr[0]<=arr[n-1]:
    #     return n-1-0
    max_index = min_index = 0
    l_min = arr[0]
    r_max = arr[n-1]
    while(i<n and j>=0):
        r_max = max(r_max,arr[j])
        l_min = min(l_min,arr[i])

        if l_min <= r_max:
            diff = max(diff, arr.index(r_max)-arr.index(l_min))

        i+=1
        j-=1

        



        
    
    return diff
    
    

            
if __name__ == "__main__":
    n = 8
    a = [31,2,4,17,19,0,1,0]
    res = max_index(a,n)
    print(res)