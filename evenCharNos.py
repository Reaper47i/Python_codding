def isEven(x):
    out = 0;
    for i in x:
        if(i%2 == 0):
            out+=i
    
    if(out > 0):
        return out
    else:
        return -1


if __name__ == "__main__":
    s = input();
    a = [];
    for i in s:
        if(i.isdigit()):
            a.append(int(i));

    out = isEven(a) 
    print(out)  

