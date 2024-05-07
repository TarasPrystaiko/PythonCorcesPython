# Find the sum and product of the elements of the list greater than the number MIN and less than the number MAX (both boundaries inclusive).
#
# If there are no such elements, print None object for both the sum and the product.
#
#Output
# lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
# MIN = 3
# MAX = 6
# ...
# sum_ = 20, product = 576

def categorize_numbers(numbers):
    divisible_by_3_not_5 = []
    divisible_by_5_not_3 = []
    divisible_by_both_3_and_5 = []

    for num in numbers:
        if num % 3 == 0 and num % 5 != 0:
            divisible_by_3_not_5.append(num)
        elif num % 5 == 0 and num % 3 != 0:
            divisible_by_5_not_3.append(num)
        elif num % 3 == 0 and num % 5 == 0:
            divisible_by_both_3_and_5.append(num)

    return divisible_by_3_not_5, divisible_by_5_not_3, divisible_by_both_3_and_5

# Input list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Categorize the numbers
result = categorize_numbers(numbers)

# Print the results
print("elements divided  by 3", result[0])
print("elements divided  by 5", result[1])
print("Divisible by both 3 and 5:", result[2])