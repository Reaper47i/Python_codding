def find_end_zeros(f):
    ''' counts the number of zeros in the fact fist by checking if %==0 then by 
        dividing it by 10 it reduces the number  '''
    count = 0
    while f:
        if f % 10 == 0:
            count += 1
        else:
            break
        f = f/10
    return count


def factorial(number):  # sourcery skip: merge-comparisons
    ''' Takes the input range of numbers of which the factorial needs to be found '''
    if number == 0 or number == 1:
        return 1
    else:
        return number*factorial(number - 1)


if __name__ == '__main__':
    n = int(input())
    fact = factorial(n)
    # print(fact)
    print(find_end_zeros(fact))
