def second_largest(nums):
    if not nums or len(set(nums)) == 1:
        return None

    max_num = float('-inf')
    second_max = float('-inf')

    # Iterate through the list
    for num in nums:
        # Update max_num if current number is greater than max_num
        if num > max_num:
            second_max = max_num  # Update second_max
            max_num = num  # Update max_num
        elif num > second_max and num != max_num:
            second_max = num  # Update second_max

    if second_max == float('-inf'):
        return None
    else:
        return second_max


# Test the function
print(second_largest([1, 2, 3, 4, 5]))  # Output: 4
print(second_largest([1, 1]))  # Output: None
print(second_largest([]))  # Output: None
