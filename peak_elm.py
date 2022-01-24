
def peak_elm_util(a,low,high,n):

    mid = int((low+high)/2)
    # for edge cases when all elm are same or length is of 2 or 1
    if((mid == 0 or a[mid-1]<=a[mid]) and (mid == n-1) or a[mid+1]<=a[mid]):
        return mid
    
    # if left of mid is greater i.e posibility of peak on l.h.s
    elif(mid>0 and a[mid-1]>a[mid]):
        return peak_elm_util(a,low,(mid-1),n)
    else:
        # posibility of peak at r.h.s
        return peak_elm_util(a,(mid+1),high,n)

def peak_elm(arr,n):
    return peak_elm_util(arr,0,n-1,n)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = peak_elm(arr,n)
    print(res)