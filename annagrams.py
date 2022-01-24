'''
Two strings are anagrams of each other
if the letters of one string 
can be rearranged to form the other string. 
Given a string, 
find the number of pairs of 
substrings of the string that are anagrams 
of each other.
'''

from collections import Counter


def anagram(s):
    size = len(s)
    c = Counter(s)    
            
    return


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s1 = input()
    
    anagram(s1)
