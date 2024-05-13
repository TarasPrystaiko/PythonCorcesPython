def second_largest(nums):
    # Check if the list is empty or contains only one element
    if not nums or len(set(nums)) == 1:
        return None

    # Initialize variables to store maximum and second maximum numbers
    max_num = float('-inf')  # Initialize with negative infinity
    second_max = float('-inf')  # Initialize with negative infinity

    # Iterate through the list
    for num in nums:
        # Update max_num if current number is greater than max_num
        if num > max_num:
            second_max = max_num  # Update second_max
            max_num = num  # Update max_num
        # Update second_max if current number is greater than second_max but less than max_num
        elif num > second_max and num != max_num:
            second_max = num  # Update second_max

    # If second_max is still negative infinity, there's no second largest number
    if second_max == float('-inf'):
        return None
    else:
        return second_max


# Test the function
print(second_largest([1, 2, 3, 4, 5]))  # Output: 4
print(second_largest([2, 2, 2, 2]))  # Output: None
print(second_largest([]))  # Output: None
