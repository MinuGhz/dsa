# time complexity = O(r)
def C(n , r):
    if r > n or r < 0:
        return 0
    if r == 0 or r == n:
        return 1
    arr1 = []
    arr2 = []
    for i in range(r):
        arr1.append(n-i)
        arr2.append(i+1)

    combination = 1
    for j in range(r):
        combination *= arr1[j]
        combination //= arr2[j]


    return combination


print(C(10,3))
