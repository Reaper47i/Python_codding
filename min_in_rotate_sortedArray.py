
def findMin_util(arr,low,high):
    if high == low:
        return arr[0]
    
    mid = int((low + (high-low))/2)

    if mid<high and arr[mid] < arr[mid-1]:
        return arr[mid]

def findMin(arr,n):
    return findMin_util(arr,0,n-1) 

if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().rstrip().split()))