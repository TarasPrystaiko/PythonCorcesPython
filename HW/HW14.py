def sort_columns(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Transpose the matrix to work with columns
    transposed_matrix = [[matrix[j][i] for j in range(num_rows)] for i in range(num_cols)]

    # Sort the columns based on the first element of each column
    transposed_matrix.sort(key=lambda x: x[0])

    # Transpose the sorted matrix back
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
