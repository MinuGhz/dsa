def modify_matrix(matrix):
    n = len(matrix)
    for row in range(n):
        for col in range(n):

            if row == col:
                matrix[row][col] += 1

            elif (row + col) == (n - 1):
                matrix[row][col] -= 1

            elif (col > row) and (row + col < n - 1):
                matrix[row][col] += 2

            elif (col < row) and (row + col > n - 1):
                matrix[row][col] -= 2

            elif (col < row) and (row + col < n - 1):
                matrix[row][col] += 3

            elif (col > row) and (row + col > n - 1):
                matrix[row][col] -= 3
    return matrix


matrix_3x3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print(modify_matrix(matrix_3x3))


