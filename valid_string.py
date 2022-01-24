'''
Sherlock considers a string to be valid 
if all characters of the string 
appear the same number of times. 
It is also valid if he can remove 
just 1 character at 1 index in the string,
and the remaining characters 
will occur the same number of times.
Given a string , determine if it is valid. 
If so, return YES, otherwise return NO.
'''

from typing import Counter

# this is done using Counter import fom collections
def valid_string(st):
    x = Counter(st)
    rem = 0
    ls = x.most_common()[-1]
    _min = ls[1]
    for i in x:
        if(_min == x[i]):
            continue
        else:
           rem+=1

    if(rem==1):
        return "YES"
    else:
        return "NO" 
        
#  non Counter method without using library

            



if __name__ == "__main__":
    s = 'aabbccddeefghi'
    result = valid_string(s)
    print(result)
