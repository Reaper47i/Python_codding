import time
import math


def if_prime(num):      # basic way of printing prime numbers
    prime_numbers = []
    for n in range(1, num+1):
        flag = 0
        if n > 1:
            for d in range(2, n):
                if n % d == 0:
                    flag += 1
            if flag == 0:
                prime_numbers.append(n)

    return prime_numbers


def prime_alt(num):         # this method is better as it calculated only half of the factors of the number from i to n untill it reaches the sqrt of that number
    prime_numbers = []
    # takes the square root of the number
    for n in range(1, num+1):
        max_divisor = math.floor(math.sqrt(n))
        flag = 0
        for j in range(2, 1 + max_divisor):
            if n % j == 0:
                flag += 1

        if flag == 0 and n > 1:
            prime_numbers.append(n)

    return prime_numbers


def primeV3(num):   # eliminates even values as they are never prime except 2 and futher enhances the sqrt method
    prime_arr = []
    for n in range(1, num+1):
        if n == 2:
            prime_arr.append(n)

        if n > 2 and n % 2 != 0:
            max_D = math.floor(math.sqrt(n))
            f = 0
            for k in range(3, max_D+1, 2):

                if n % k == 0:
                    f += 1
            if f == 0:
                prime_arr.append(n)
    return prime_arr


if __name__ == "__main__":
    n = int(input())
    t0 = time.time()

    print(if_prime(n))
    print(prime_alt(n))
    print(primeV3(n))
    t1 = time.time()
    print(t1-t0)
