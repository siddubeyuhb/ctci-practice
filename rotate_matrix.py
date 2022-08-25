# Cracking the Coding Interview Q 1.7 Rotate Matrix

# Rotate a NxN matrix clockwise by 90 degrees

def rotate(mat):
    n = len(mat)  # Assuming it is NxN matrix
    new = [[0] * n for i in range(n)]  # NxN matrix of 0s

    for i in range(n):
        for j in range(n):
            new[j][n - 1 - i] = mat[i][j]

    return new


matrix1 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]

matrix2 = [[1, 2],
           [3, 4]]

matrix3 = [[1]]

print(rotate(matrix1))
print(rotate(matrix2))
print(rotate(matrix3))
