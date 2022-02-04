n = 9
s = ''
for i in range(n):
    if i%2 == 0:
        s+='{'
    else:
        s+='}'

print(s)
print(s.pop())