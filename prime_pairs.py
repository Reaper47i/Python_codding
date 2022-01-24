import math
import time


def prime_pairs(prime_arr):
    for i in range(len(prime_arr)+1):
        if i == len(prime_arr)-1:
            break

        if prime_arr[i+1] - prime_arr[i] == 2:
            print(str(prime_arr[i]) + " " + str(prime_arr[i+1]))


def if_prime(num):
    pArr = []
    for n in range(1, num+1):
        if n == 2:
            pArr.append(n)

        if n > 2 and n % 2 != 0:
            max_divisor = math.floor(math.sqrt(n))
            flag = 0
            for d in range(3, 1+max_divisor, 2):
                if n % d == 0:
                    flag += 1

            if flag == 0:
                pArr.append(n)
    return pArr


if __name__ == '__main__':
    n = int(input())
    t0 = time.time()
    arr = if_prime(n)
    prime_pairs(arr)

    t1 = time.time()
    print(t1-t0)
