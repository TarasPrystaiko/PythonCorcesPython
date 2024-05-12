def lst2dict(lst):
    # Initialize an empty dictionary
    result_dict = {}

    list_length = len(lst) if len(lst) % 2 == 0 else len(lst) - 1

    for i in range(0, list_length, 2):
        result_dict[lst[i]] = lst[i + 1]

    return result_dict


# Test the function
print(lst2dict([0, 1, 2, 3]))  # Output: {0: 1, 2: 3}
print(lst2dict(['a', 'A', 'b', 'B', 'c']))  # Output: {'a': 'A', 'b': 'B'}
