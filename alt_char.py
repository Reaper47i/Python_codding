
def alt_char(a):
    x = []
    remove = 0
    for i in range(len(a)-1):
        if(a[i]==a[i+1]):
            remove+=1
    
    return remove
        
        
            



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        res = alt_char(s)
        print(res)



