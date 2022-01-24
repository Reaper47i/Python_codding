a = [28 ,7 ,-36 ,21 ,-21 ,-50 ,9 ,-32]
a.sort()
print(a)
r = [0]*2
k = 1
_sum = 0
for i in range(len(a)):
    _sum += a[i]
    r[0]=_sum
    r[1] = i

print(r)

