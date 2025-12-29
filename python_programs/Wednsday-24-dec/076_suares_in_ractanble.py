def count_no_of_squares(a, b):
    matrix = [[1]*b for _ in range(a)]
    
    for i in range(1, a, 1):
        for j in range(1, b, 1):
            if matrix[i][j] == 1:
                matrix[i][j] = 1 +  min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])
    
    count = 0
    for i in range(a):
        for j in range(b):
            count += matrix[i][j]

    return count

print(count_no_of_squares(3, 3))