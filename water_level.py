'''

given an array of walls
need to find water level present b/w them
each element in array represents on block 
of value 1
[3,1,0,0,2]
3-> blocks of 1 unit
2-> blocks of 1 unit
0-> no block
2-> 2blocks of 1 unit
total water
1+

'''

def water_level(arr,n):
    left_max = right_max = 0
    l = 0
    r = n-1
    water = 0

    while(l<=r):
        if right_max<=left_max:
            water += max(0,right_max-arr[r])
            right_max = max(right_max,arr[r])
            r-=1
        else:
            water+=max(0,left_max-arr[l])
            left_max = max(left_max,arr[l])
            l+=1

        
    return water

    

if __name__ == "__main__":
    n = 7
    a = [8 ,8 ,2 ,4 ,5 ,5 ,1]
    res = water_level(a,n)
    print(res)