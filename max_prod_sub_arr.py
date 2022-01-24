'''
GFG code below for this problem =>
	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
	    # Variables to store maximum and
	    # minimum product till ith index.
	    minVal = arr[0]
	    maxVal = arr[0]

	    maxProduct = arr[0]

	    for i in range(1, n, 1):

	        # When multiplied by -ve number,
	        # maxVal becomes minVal
	        # and minVal becomes maxVal.
	        if (arr[i] < 0):
	            temp = maxVal
	            maxVal = minVal
	            minVal = temp

	        # maxVal and minVal stores the
	        # product of subarray ending at arr[i].
	        maxVal = max(arr[i], maxVal * arr[i])
	        minVal = min(arr[i], minVal * arr[i])

	        # Max Product of array.
	        maxProduct = max(maxProduct, maxVal)

	    # Return maximum product
	    # found in array.
	    return maxProduct
'''



def max_prod(arr,n):
    _min = arr[0]
    _max = arr[0]
    res = arr[0]

    for i in range(1,n):
        if arr[i] == 0:
            _min = 1
            _max = 1
            continue
        
        temp1 = arr[i] * _max
        temp2 = arr[i] * _min
        _max = max(temp1, temp2)
        _max = max(_max, arr[i])
        _min = min(temp1,temp2)
        _min = min(_min, arr[i])

        res = max(res, _max)
    
    return res


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    res = max_prod(a,n)
    print(res)