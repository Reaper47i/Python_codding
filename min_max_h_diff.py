'''

if arr[i] < k arr[i] + k
if arr[i] > k arr[i] - k

'''

def min_max_h(arr,n,k):
    final_diff = 0
    res = set()

    for i in range(n):
        if arr[i]<k:
            temp1 = arr[i] + k
        else:
            temp1 = arr[i] - k

        res.add(temp1)
    
    max_h = max(res)
    min_h = min(res)
    final_diff = max_h - min_h

    return final_diff



if __name__ == "__main__":
    n = 6
    k = 4
    a = [1,6,2,7,9,10]
    ans = min_max_h(a,n,k)
    print(ans)


    '''
    GFG solution to the problem =>

    def minJumps(arr, n):
        
        if len(arr) <= 1 : 
            return 0 
  
        # Return -1 if not possible to jump 
        if arr[0] == 0 :  
            return -1 
  
        # initialization 
        maxReach = arr[0]; 
        step = arr[0]; 
        jump = 1; 
  
  
        # Start traversing array 
        for i in range(1,len(arr)):

            # Check if we have reached the end of the array 
            if  i == len(arr) - 1 : 
                return jump 
  
            # updating maxReach 
            maxReach = max(maxReach, i+arr[i])
  
            # we use a step to get to the current index 
            step-=1; 
  
            # If no further steps left 
            if  step == 0 : 
                #  we must have used a jump 
                jump+=1 
                   
                #Check if the current index/position  or lesser index 
                #is the maximum reach point from the previous indexes 
                if i>=maxReach : 
                   return -1
  
                #re-initialize the steps to the amount 
                #of steps to reach maxReach from position i. 
                step = maxReach - i 
  
        return -1    

if __name__ == "__main__":
    n = 10
    a = [2 ,3 ,1 ,1 ,2 ,4 ,2 ,0 ,1 ,1]
    ans = minJumps(a,n)
    print(ans)
    
    
    '''