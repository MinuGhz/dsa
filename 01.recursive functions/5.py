def max_finder(array, n , i =0, max = 0):
    if i==0:
        max = array[i]
        return max_finder(array, n , i+1 , max)
    elif i==n-1:
        if max<array[i]:
            max = array[i]
        return max

    else:
        if max < array[i]:
            max = array[i]
        return max_finder(array, n , i+1 , max)



print(max_finder([1,4,6,2,3,12,4], 7))