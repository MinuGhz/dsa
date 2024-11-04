def pascal_triangle(levels):
    triangle = [[1]]

    for i in range(1, levels):
        new_row = [1]
        for j in range(1, i):
            new_row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle


levels = 4
pascal = pascal_triangle(levels)
for line in pascal:
    print(line)
