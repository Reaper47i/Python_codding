'''
we impliment an array to a waveform
which is like:-
a[0]>=a[1]<=a[2]>=a[3]<=a[4]>=.....a[n-1]<=a[n]

1 2 3 4 5 6 --> 2 1 4 3 6 5 
0 1 2 3 4 5
 // len = 5
i = 1,
 n - range

1 2 3 4 5

'''



    

def conv_to_wave(arr,n):
    i = 1
    while(i<n-1):
        if i%2 != 0:
            if arr[i-1]<arr[i]:
                temp = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = temp
            if arr[i]>arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
        else:
            if arr[i]<arr[i-1]:
                temp = arr[i-1]
                arr[i-1] = arr[n]
                arr[i] = temp
            if arr[i]<arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp 

        i+=1

    return arr



if __name__ == "__main__":
    n = 6
    a = [22,45,90,103,23,1]
    conv_to_wave(a,n)
    print(*a)