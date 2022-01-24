def comm_sub_string(a,b):
    out = False
    for i in range(len(a)):
        if(a[i] in b):
            out = True
        
    if(out):
        print("Yes")
    else:
        print("No")
            
    
    
    return

if __name__ == "__main__":
    t = int(input())
    s1 = input()
    s2 = input()
    comm_sub_string(s1,s2)