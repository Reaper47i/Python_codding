def comp(_ls):
    score = []
    low2 = 0
    out = []
    for i in range(len(_ls)):
        if _ls[i][1] not in score:
            score.append(_ls[i][1])


    for j in range(2):
        low2 = score.pop(score.index(min(score))) 
    
    for k in range(len(_ls)):
        if(low2 == _ls[k][1]):
            out.append(_ls[k][0])
    
    out.sort()
    
    return out
         

if __name__ == '__main__':
    stu_ls = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stu_ls.append([name,score])
    
    out_ls = comp(stu_ls)
    for j in out_ls:
        print(j)