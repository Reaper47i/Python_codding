'''
write a programe to implement the different stack func(s)
and impliment them in two arrays

'''

from collections import deque


def push1(arr,num):
    arr.append(num)
    return arr
    
def push2(arr,num):
    arr.append(num)
    return arr

def pop1(arr):
    arr.pop()
    return arr

def pop2(arr):
    arr.pop()
    return arr

def insert1():
    pass

def insert2():
    pass

def q_check(q):
    res_arr1 = deque()
    res_arr2 = deque()
    for i in range(len(q)):
        if q[i][0] == 'push1':
            push1(res_arr1,q[i][1])
        
        if q[i][0] == 'push2':
            push2(res_arr2,int(q[i][1]))

        if q[i][0] == 'pop1':
            pop1(res_arr1)

        if q[i][0] == 'pop2':
            pop2(res_arr2)


          
    print(*res_arr1)
    print(*res_arr2)


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        querries = []

        q=''
        num = 0
        for i in range(n):
            q,num = input().split() 
            querries.append([q,num])
        
        q_check(querries)

        # print(querries)


