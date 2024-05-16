def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

# Test the function
nested_list = [1, [2, 3], [4, [5, 6]], 7, [8, [9, 10]]]
result = flatten(nested_list)
print(result)