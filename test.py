c_a = dict()
# c_b = dict()
flag = False
a = [3231 ,53858 ,19 ,5 ,59 ,498 ,520 ,7 ,9 ,10 ,11 ,12]
b = [520 ,7 ,498 ,59 ,10 ,6 ,12]

for i in a:
    if i in c_a:
        c_a[i]+=1
    else:
        c_a[i]=1

for j in b:
    if j in c_a:
        c_a[j]+=1

for k in b:
    if c_a[k]==2:
        flag = True
    else:
        flag = False
        print("No")




print(c_a)    




if flag:
    print("yes")
else:
    print("no")