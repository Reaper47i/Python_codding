
from tokenize import String


def parn_util(op,cl,s,out):
    if op == 0 and cl == 0:
        out.append("".join(s))
        return
    
    if op!=0:
        s.append('(')
        parn_util(op-1,cl,s,out)
        s.pop()
        
    if cl>op:
        s.append(')')
        parn_util(op,cl-1,s,out)
        s.pop()
            
    
    

def gen_parn(n):
    s = []
    out = []
    op = n
    cl = n
    parn_util(op,cl,s,out)
    
    return out



if __name__ == "__main__":
    n = int(input())
    res = gen_parn(n)
    print(*res)