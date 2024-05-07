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

def sum_and_product(lst, MIN, MAX):
    # Initialize variables to hold the sum and product
    sum_result = None
    product_result = None

    for num in lst:
        if MIN <= num <= MAX:
            if sum_result is None:
                sum_result = 0
                product_result = 1

            sum_result += num
            product_result *= num

    return sum_result, product_result

# Test input
lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
MIN = 3
MAX = 6

sum_result, product_result = sum_and_product(lst, MIN, MAX)

#Print
print("Sum:", sum_result)
print("Product:", product_result)