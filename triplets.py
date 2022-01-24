'''
counting triplets in a G.P

'''

from itertools import combinations


def triplets(arr,r):
    sub = list(combinations(arr,3))
    res = []
    
    for i in range(len(sub)):
        fst = sub[i][0]
        snd = sub[i][1]
        thrd = sub[i][2]
        if(snd/r == fst and snd*r == thrd):
            res.append(sub[i])
      

    return len(res) 




if __name__ == "__main__":
    # sz,r = [int(x) for x in input().split()]
    sz = 4
    r = 5
    A = [1,5,5,25,125]
    # A = list(map(int,input().rstrip().split()))
    res = triplets(A,r)
    print(res)
    