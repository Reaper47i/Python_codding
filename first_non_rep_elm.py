from collections import defaultdict


def non_rep_elm(arr, n):
    c_arr = defaultdict(lambda:0)
    
    for i in range(n):
        c_arr[arr[i]]+=1

    print(c_arr)
    for j in c_arr:
        if c_arr[j] == 1:
            return j



if __name__ == "__main__":
    n = 20
    a = [-1,-17, -12, 8, 16, -17, -13, -14, -3, -6, -5, -11, -10, -12, -5, 19, -17, -5, -1, 12]
    ans = non_rep_elm(a,n)
    print(ans)