def sort_matrix_by_row_sum(matrix):
    return sorted(matrix, key=sum)

def sort_matrix_by_row_sum_reverse(matrix):
    return sorted(matrix, key=sum, reverse=True)


matrix = [
    [3, 1, 2],   # 6
    [4, 0, 1],   # 5
    [2, 2, 2],   # 6
    [1, 1, 1]    # 3
]

result = sort_matrix_by_row_sum(matrix)
print(result)
print(sort_matrix_by_row_sum_reverse(matrix))
