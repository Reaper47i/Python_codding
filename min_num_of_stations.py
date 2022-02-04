'''
Find the min num of platforms needed for the smooth functioning
of all the trains in the stations
'''


def min_plat(arr,dep,n):
    arr.sort()
    dep.sort()
    plat = 1
    min_plat_nedded = 1
    i = 1
    j = 0

    while(i<n and j<n):
        if (arr[i]<=dep[j]):
            plat+=1
            i+=1

        elif (arr[i]>dep[j]):
            plat-=1
            j+=1
        
        if plat>min_plat_nedded:
            min_plat_nedded = plat
    
    
    return min_plat_nedded
    


if __name__ == "__main__":
    n = 6
    arival = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    res = min_plat(arival,dep,n)
    print(res)

