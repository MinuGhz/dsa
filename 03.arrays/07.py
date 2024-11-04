def ifTransforce(A , B):
    BB = []
    arr = []
    for i in range(len(B)):
        for j in range(len(B[0])):
            if A[i][j] != B[j][i]:
                return False

    return True



A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

B = [
    [1,4,7],
    [2,5,8],
    [3,6,9]
]

C = [
    [1,3,3],
    [4,5,7],
    [9,10,30]
]
print(ifTransforce(A,B))
print(ifTransforce(A,C))
