

from typing import Counter

        
def anagram(a,b):
    x = Counter(a)
    y = Counter(b)
    count = 0

    if x == y:
        return 0
    else:
        x.subtract(y)
        count = (sum(abs(i) for i in x.values()))
        return count    

    # if x == y :
    #     return 0 
    # else:
    #     for i in a:
    #         if i not in b:
    #             count += 1
    #     for j in b:
    #         if j not in a:
    #             count += 1
        
    #     return count

    

if __name__ == "__main__":
    # s1 = input()
    # s2 = input()
    s1 = 'fcrxzwscanmligyxyvym'
    s2 = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke' 
    res = anagram(s1,s2)
    print(res)



# jxwtrhvujlmrpdoqbisbwhmgpmeoke
# fcrxzwscanmligyxyvym