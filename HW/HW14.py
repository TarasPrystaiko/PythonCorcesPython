def sort_columns(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    transposed_matrix = [[matrix[j][i] for j in range(num_rows)] for i in range(num_cols)]

    transposed_matrix.sort(key=lambda x: x[0])

    sorted_matrix = [[transposed_matrix[j][i] for j in range(num_cols)] for i in range(num_rows)]

    return sorted_matrix

# Example usage:
matrix = [
    ['a', 'f', 'e'],
    ['c', 'b', 'l'],
    ['e', 'a', 'i'],
    ['k', 'n', 'a']
]

sorted_matrix = sort_columns(matrix)
for row in sorted_matrix:
    print(row)
