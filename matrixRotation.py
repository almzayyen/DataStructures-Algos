

def rotate_matrix(matrix, r):
    n = len(matrix)
    m = len(matrix[0])
    r = r % (n * m)  # in case r > n*m
    # Transpose the matrix
    for i in range(n):
        for j in range(i, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]

    # Reverse the columns of the first r rows
    for i in range(r):
        matrix[i] = matrix[i][::-1]
    return matrix
