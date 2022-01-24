'''
length of the longest occuring seq. in an array
'''


def long_consq(arr,n):
    curr_seq = 0
    longest_seq = 0
    s = set()
    for i in arr:
        s.add(i)

    for j in range(n):
        if arr[j] - 1 not in s:
            curr_no = arr[j]

            while(curr_no in s):
                curr_seq+=1
                curr_no+=1
            
            longest_seq = max(longest_seq,curr_seq)
            
        curr_seq = 0
    
    return longest_seq
    

if __name__ == "__main__":
    n = 7
    a = [2 ,6 ,1 ,9 ,4 ,5 ,3]
    ans = long_consq(a,n)
    print(ans)