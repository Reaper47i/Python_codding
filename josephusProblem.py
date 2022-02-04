'''
I/P => (n,k)
In scenario we have n number of people standing in a circle
we need to kill the kth persson so the k-1 is saved
this circular game plays on until one of them is left

move circularly by (i+k)%n

can be done in 2 ways recursively or using bit manupilation

'''
# using bit manupilation

def jp_bit_mp(n):
    b_arr = [x for x in (format(n,"b"))]
    num = b_arr.pop(0)
    b_arr.append(num)
    
    res = int("".join(b_arr),2)
    
    return res


# folowing solution using recursion
def jp(n,k):  
    if(n==1):
        return 1
    else:
        return (jp(n-1,k)+k-1)%n+1
    
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    # res = jp(n,k)
    # print(res)
    print(jp_bit_mp(n))