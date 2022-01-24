'''
swapping array into alternate positions of 
first +ve then -ve 
the algo uses similar swaping technique as used in merge sort
'''


def alter_pos(arr,n):
    pos = []
    neg = [] 
    res = [0]*n
    for i in arr:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
    
    i = j = k = 0
    print(pos,neg)
    while(i<len(pos) and j < len(neg)):
        res[k] = pos[i]
        i+=1
        k+=1
        res[k] = neg[j]
        j+=1
        k+=1

    while(i<len(pos)):
        res[k] = pos[i]
        i+=1
        k+=1

    while(j<len(neg)):
        res[k] = neg[j]
        j+=1
        k+=1

    return res 


if __name__ == "__main__":
    n = 9
    a = [9, 4, -2, -1, 5, 0, -5, -3, 2]
    ans = alter_pos(a,n)
    print(ans)