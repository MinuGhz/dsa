def insertionSort_2D(arr):
    m = len(arr)
    n = len(arr[0])

    if m <= 1 or n <=1:
        return
    for i in range(m):
        for j in range(1, n):
            key = arr[i][j]
            x = j - 1
            while x >= 0 and key < arr[i][x]:
                arr[i][x + 1] = arr[i][x]
                x -= 1
            arr[i][x + 1] = key  # Insert the key in the correct position


arr = [[12, 11, 13, 5, 6],[4,5,23,1,65],[34,23,12,2,67]]
insertionSort_2D(arr)
print(arr)
