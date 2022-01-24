'''
The stock span problem is a financial problem 
where we have a series of n daily price quotes
for a stock and we need to calculate the span
of stocks price for all n days. 
The span Si of the stocks price on a given day i 
is defined as the maximum number of consecutive days just before the given day, 
for which the price of the stock on the current day is less than or equal to its price on the given day.
For example, 
if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, 
then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.
'''

# Brute force aproach
def stock_span(arr,n):
    span = [1]

    for i in range(1,n):
        temp = 0
        if arr[i]<arr[i-1]:
            span.append(1)
        else:
            for j in range(i,-1,-1):
                if arr[i] >= arr[j]:
                    temp+=1
                else:
                    break
            
            span.append(temp)
    
    return span
    



if __name__ == "__main__":
    N = 7
    price = [100, 80, 60, 70, 60, 75, 85]
    ans = stock_span(price,N)
    print(ans)