# fibo and fact using recursion
def fibo(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1

    else:
        a = fibo(n-1)
        b = fibo(n-2)
        return a+b

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


if __name__ == "__main__":
    n = int(input())
    
    # for i in range(n):
    #     print(fibo(i))
    
    print(fact(n))