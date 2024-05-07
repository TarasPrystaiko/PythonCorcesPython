# There is a two-dimensional list of Latin letters. Sort the letters by columns.
#
# We assume that the list is rectangular.
#
# DO NOT use built-in functions map and zip.
#
#Output
# [['a', 'c', 'e']
#  ['f', 'b', 'a']
#  ['a', 'n', 'k']
#  ['e', 'l', 'i']]
# # ->
# [['a', 'b', 'a']
#  ['a', 'c', 'e']
#  ['e', 'l', 'i']
#  ['f', 'n', 'k']]
def sort_columns(matrix):
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    sorted_transposed = [sorted(row) for row in transposed_matrix]

    sorted_matrix = [[sorted_transposed[j][i] for j in range(len(sorted_transposed))] for i in
                     range(len(sorted_transposed[0]))]

    return sorted_matrix


# Test input
matrix = [['a', 'c', 'e'],
          ['f', 'b', 'a'],
          ['a', 'n', 'k'],
          ['e', 'l', 'i']]

sorted_matrix = sort_columns(matrix)

# Print the sorted matrix
for row in sorted_matrix:
    print(row)
