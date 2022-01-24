def bitwiseOr(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans |= arr[i]
        print(ans)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().rstrip().split()))
        res = bitwiseOr(A)
        print(res)