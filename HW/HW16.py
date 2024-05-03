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