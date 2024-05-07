# There is a list of at least two float elements.
#
# Create a new list. It should contain elements of initial list, and between them should be added average of that elements.
#
#Output
# lst = [1, 2, 3, 4, 5]
# Result: [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
def insert_average(lst):
    result = []
    for i in range(len(lst) - 1):
        result.append(lst[i])
        result.append((lst[i] + lst[i + 1]) / 2)
    result.append(lst[-1])
    return result

# Test input
lst = [1, 2, 3, 4, 5]

result = insert_average(lst)

# Print the result
print(result)