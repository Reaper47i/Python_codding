def odd(n):
    ans = []
    q = (n/4);
    r = n%4;
    gr = n + (4+r);
    sm = n - r;
    multiple = 0
    if(gr - n > n - sm):
        multiple = sm/4;
    else:
        multiple = gr/4;

    diff = 0
    for j in range(4):
        if(diff > multiple):
            ans.append(multiple);
            diff = n - diff   
        else:
            ans.append(diff);
    
    return ans
def even(n):
    ans = []
    df = abs(n/4)
    for i in range(4):
        ans.append(df)
    return ans
if __name__ == '__main__':
    x = int(input())
    out = []
    if(x%2==0):
        out = even(x)
    else:
        out = odd(x)
        
    
    print(' '.join(map(str, out)))


