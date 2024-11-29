def Bubble_max(arr):

    for i in range(3):
        for j in range(len(arr)-1):
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    print(arr)

    return arr[1]




arr = [6,3,12,5,8,1]
second_max = Bubble_max(arr)
print(second_max)