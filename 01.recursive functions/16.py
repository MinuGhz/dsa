def sub_array(array , index = 0 , current_subarray = None):
    if current_subarray is None:
        current_subarray = []

    if index== len(array):
        print(current_subarray)
        return

    sub_array(array , index+1 , current_subarray + [array[index]] )

    sub_array(array, index + 1, current_subarray)



sub_array([1,2,3])

