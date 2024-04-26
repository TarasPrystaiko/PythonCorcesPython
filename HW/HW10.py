# Task10:
# The user enters a string. Print True if the string is a palindrome, otherwise False.
# A palindrome is a string that reads the same way from the left and from the right.
# If there are leading or trailing spaces in the line, they should not be taken into account.
# The check must be case-insensitive.
# Solve at least in TWO ways.

# "    aBC cba " # True
# "a BCQcb a    " # True
# " ab bca"  # False
# "ab b a"  # False


# Solution10:
user_input = input("Enter a string: ")
def is_palindrome_method1(s):
    s = s.strip().lower()
    reversed_s = s[::-1]
    return s == reversed_s


result_method1 = is_palindrome_method1(user_input)

print(result_method1)


user_input = input("Enter a string: ")

length = len(user_input)
i = 0
j = length - 1

while i < j:
    if user_input[i] != user_input[j]:
        print(user_input, "False")
        break
    i += 1
    j -= 1
else:
    print(user_input, "True")