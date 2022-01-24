def sub_arr_sum(arr,k):
    _sum = 0
    n = len(arr)

    for i in range(n-1):
        _sum = arr[i]
        for j in range(i+1,n):
            _sum += arr[j]

            if _sum == k:
                return True
            else:
                continue
    
    return False



if __name__ == "__main__":
    k = int(input())
    a = [4,2,-3,1,6]
    ans = sub_arr_sum(a,k)
    print(ans)