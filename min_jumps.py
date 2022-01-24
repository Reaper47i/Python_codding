def min_jumps(arr,n):
    steps = 0    
    jump = 0
    _range = arr[0]
    
    for i in range(n):
        pos = i
        step = arr[i]
        max_step = max(max_step,step)
        if pos == step:
            jump+=1
        


    


if __name__ == "__main__":
    n = 10
    a = [2 ,3 ,1 ,1 ,2 ,4 ,2 ,0 ,1 ,1]
    res = min_jumps(a,n)
    print(res)



'''
for every element we need to check the
within the range the max element 
1. take 3 vars :- max_reachable, steps, jumps
2. 

'''