
def permute_util(s,ans,o):
    if(len(s) == 0):
        o.append(ans)
    
    for i in range(len(s)):
        ch = s[i]
        left_sub_str = s[0:i]
        right_sub_str = s[i+1:]
        rest = left_sub_str + right_sub_str
        permute_util(rest, ans+ch,o)

    return o

def permu(str):
    out = []
    if len(str)<1:
        return out.append(-1)
    else:
        out = (permute_util(str,"",out))

    res = []
    for i in out:
        if i not in res:
            res.append(i)

    return res

    

if __name__ == "__main__":
    s = input()
    ans = permu(s)
    print(*ans)