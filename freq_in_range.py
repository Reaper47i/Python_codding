from typing import Counter


A = [4,4,6,5,3,3,3,9]
Q = [[1,4],[2,7],[3,7],[5,6]]
ans = []
c = dict()
for i in A:
    if i in c:
        c[i]+=1
    else:
        c[i] = 1
res = []
for i in range(len(Q)):
    for j in range(Q[i][0],Q[i][1]):
        for k in c:
            if(j == c[k]):
                ans.append(k*c[k])
    res.append(sum(ans))
    ans = [0]

print(res)   

                


print(ans)
