def reverse_array(array, n , i=0):
    if i==n-1:
        print(array[i])
    else:
        reverse_array(array,n,i+1)
        print(array[i])



reverse_array([1,2,3,4,5] , 5)