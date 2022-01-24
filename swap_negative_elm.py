'''
swaping all -ve and +ve elements to one side
+ve to left
-ve to right
without changing their order
'''

'''
the following function def m_sort may be followed if they 
need to be sorted in ascending order

'''

def m_sort(Ar):
    if len(Ar)>1:
        mid = len(Ar)//2

        L = Ar[:mid]
        R = Ar[mid:]

        m_sort(L)
        m_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if(L[i]<R[j]):
                Ar[k] = L[i]
                i+=1
            else:
                Ar[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            Ar[k] = L[i]
            i+=1
            k+=1
        
        while j < len(R):
            Ar[k] = R[j]
            j+=1
            k+=1




def swap_one_side(arr,n):
    L_positive = []
    R_negative = []
    for i in range(n):
        if arr[i] > 0:
            L_positive.append(arr[i])
        else:
            R_negative.append(arr[i])

    # only when they need to be sorted in ascending order
    # m_sort(L_positive)
    # m_sort(R_negative)
    # for sorting in the order of their appearence
    # i.e without changing order
    # we return the segregated elms from 
    # L_positive and R_negative
    # only when out is new arr
    # return L_positive+R_negative
    # if out is smae array

    new_arr = L_positive+R_negative
    
    for i in range(len(new_arr)):
        arr[i] = new_arr[i]


if __name__ == "__main__":
    # n = int(input())
    n = 8
    A = [1,-1,3,2,-7,-5,11,6]
    swap_one_side(A,n)
    print(*A)
