
# right side pattern
def staircase(n):
    k = n-1
    for x in range(n):
        for y in range(k):
            print(end=" ")
        k = k-1

        for j in range(0, x+1):
            print("* ", end="")

        print("\r")


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

# left side pattern

'''
def leftStair(n):
    for i in range(n):
'''
