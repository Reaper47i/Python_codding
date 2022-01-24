'''
# we need to create a cashier system:-
the system first checks if there is 
any stock available of the item
and then we calculate the price
and then then print out the total
and number of items

'''
def display_out(_stk,_tot):
    for i in range(len(_stk)):
        print(_stk[i], ">>>>", _tot[1][i])

    print("TOTAL AMMOUNT :",_tot[0])


        
def total(_ls,_price):
    sub_total = []
    total = sum = 0;
    for i in range(len(_ls)):
        sum = _ls[i] * _price[i]
        sub_total.append(sum)
        total = total + (_ls[i] * _price[i]);
    
    return total,sub_total




def checkItem(x,y,z):
    size = len(y);
    check = [0]*size;

    for item in x:
        if(item == 'A'):
            check[0]+=1;
        elif(item == 'B'):
            check[1]+= 1;
        elif(item == 'C'):
            check[2]+=1;
        elif(item == 'D'):
            check[3]+=1;
        elif(item == 'E'):
            check[4]+=1;
        elif(item == 'F'):
            check[5]+=1;     
        else:
            continue
    
    for j in range(len(z)):
        if(check[j] <= z[j]):
            continue
        else:
            print("not enough in stock for", y[j])
            continue    
        

    return check


if __name__ == "__main__":
    stkItems = ['A','B','C','D','E','F'];
    stkPrice = [80, 40, 35, 40, 50, 45];
    stkAvail = [2, 3, 4, 4, 3, 2];

    # byItems = ['A','A','B','B','C','D','E','F']
    byItems = list(map(str,input().rstrip().rsplit()))
    # print(byItems);
    ck_list = checkItem(byItems,stkItems,stkAvail);
    ls_total = total(ck_list,stkPrice);
    # print(ls_total)
    display_out(stkItems,ls_total);
    

    