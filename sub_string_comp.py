# taking multiple inputs by using 
# [int(x) for x in input().split()]
# this takes two string inputs and converts them 
# into int by type conv. int()

from collections import Counter

def check(mag, note):
    a = Counter(mag)
    b = Counter(note)
    return "Yes" if (a&b)==b else "No"

    

if __name__ == "__main__":
    m,n = [int(x) for x in input().split()]
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    print(check(magazine,note))
    
    