matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(matrix[0][2])
print(matrix[1][1])
print(matrix[2][0])

for row in matrix:
    for item in row:
        print(item)
