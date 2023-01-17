def matrixRotation(matrix, r):
    n, m = len(matrix), len(matrix[0])

    for k in range(min(n, m)//2):
        layer = []
        rotation = r % (2 * (n+m-2-4*k))
        #This line calculates the number of positions by which the current layer of the matrix needs to be rotated. It does this by taking the input rotation value "r" and performing a modulo operation with the expression "(2 * (n+m-2-4*k))".

        #The expression "2 * (n+m-2-4*k)" calculates the total number of elements in the current layer. It does this by first adding the number of rows "n" and the number of columns "m" of the matrix, then subtracting 2 to account for the corners of the matrix, and finally subtracting 4 times the current layer number "k" to account for the fact that each inner layer has 4 less elements than the previous one.

        #The modulo operation with "r" ensures that the rotation value stays within the range of the number of elements in the current layer, so that the rotated position stays within the current layer.

        #top
        for i in range(k, m-k):
            layer.append(matrix[k][i])
        #right
        for i in range(k+1, n-k-1):
            layer.append(matrix[i][m-k-1])
        #bottom
        for i in range(m-k-1, k-1, -1):
            layer.append(matrix[n-k-1][i])
        #left
        for i in range(n-k-2, k, -1):
            layer.append(matrix[i][k])

        l = 0
        #top
        for i in range(k, m-k):
            matrix[k][i] = layer[(l+rotation) % len(layer)]
            l += 1
        #right
        for i in range(k+1, n-k-1):
            matrix[i][m-k-1] = layer[(l+rotation) % len(layer)]
            l += 1
        #bottom
        for i in range(m-k-1, k-1, -1):
            matrix[n-k-1][i] = layer[(l+rotation) % len(layer)]
            l += 1
        #left
        for i in range(n-k-2, k, -1):
            matrix[i][k] = layer[(l+rotation) % len(layer)]
            l += 1

    for i in matrix:
        print(" ".join(map(str, i)))

if __name__ == '__main__':
    mnr = input().rstrip().split()
    m = int(mnr[0])
    n = int(mnr[1])
    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
