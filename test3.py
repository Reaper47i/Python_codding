'''
check all the anagrams of substring
that can be formed by taking the positions 
from 0 to n
'''

from collections import Counter


s = input()
a = dict(enumerate(s,0))
print(a)
c = Counter(s)
for i in s:
    print(s(i))
    
    


# from collections import Counter

# s = input()
# print(Counter(s))
# # print(a)
# # print(a)






# a = dict(enumerate(s,0))
# for i in a.values():
#     if i in b:
#         b[i]+=1
#     else:
#         b[i] = 1
    
# print(b)