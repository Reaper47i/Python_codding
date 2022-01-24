def rotate_left(list, no_of_rotates):
    '''for i in range(len(list)):
        if i <= no_of_rotates-1:
            var = list.pop(0)
            list.append(var)
        else:
            break

    return list'''


'''    for value in (list[no_of_rotates:] + list[0:no_of_rotates]):
        return value
'''

if __name__ == '__main__':
    #n = int(input())
    d = int(input())
    Arr = [1, 2, 3, 4, 5]

    '''for i in range(n):
        Arr.append(int(input()))
'''
    #new_array = rotate_left(Arr, d)
    #print(new_array, end='')

    ''' Below is the most simple solution that can be possible in an list of elements to rotate it left
        |
        |
        |
        \/
    '''

    for value in (Arr[d:] + Arr[0:d]):
        print(value, end='')
