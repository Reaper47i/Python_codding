'''
Program to find 2nd greatest no. in a list =>
things needed to keep in mind while working with such problems :=
@ there can be multiple simmilar inputs
@ we need to simpligy them 
@then find 2nd max using max() func.
 
'''



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    ls = [] 
    [ls.append(x) for x in arr if x not in ls];
    for i in range(2):
        max2 = ls.pop(ls.index(max(ls)))
    
    print(max2)