from array import *
arr = array('i', [])
i = int(input(""))

for x in range(i):
    arr.append(int(input("")))

count = 0

for y in range(len(arr)):
    if arr[y] == 1:
        count += 1

print(count)
