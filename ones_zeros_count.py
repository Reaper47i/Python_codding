'''
most efficent way by my knowledge to calculate
the no of equal ones and zeros in the substring
it can be also used as to find the number of equal 
characters in the sub string by making all the distinct 
characters comparable.

'''

def ones_zeros(arr):
    l = len(arr)
    count = 0
    _sum = 0  
    sum_map = {0:1}

    for i in range(l):
        if arr[i] == 0:
            _sum+= -1
            if _sum in sum_map:
                sum_map[_sum]+=1
            else:
                sum_map[_sum] = 1
        else:
            _sum+= 1
            if _sum in sum_map:
                sum_map[_sum]+=1
            else:
                sum_map[_sum] = 1

        if sum_map[_sum] > 1:
            count += sum_map[_sum] -1

    return count

if __name__ == "__main__":
    a = [1,0,0,1,0,1,1]
    res = ones_zeros(a)
    print(res)