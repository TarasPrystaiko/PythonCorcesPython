#here is a list consisting of integer numbers.

# Create three lists:
#
# - to the first list add numbers that are only divisible by 3, but not divisible by 5
#
# - to the second list add numbers that are divisible by 5, but not divisible by 3
#
# - to the third list add numbers that are divisible by both 3 and 5
#
#Output
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Input list
# [3, 6, 9, 12]  # elements divided by 3
# [5, 10]  # elements divided by 5
# [0, 15]  # elements divided by 3 and by 5


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
