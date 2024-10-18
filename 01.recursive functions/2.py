def average(array, n, i=0):
    if i==n-1:
        return array[i]/n
    else:
        return array[i]/n + average(array,n,i+1)



print(average([1,2,3] , 3))