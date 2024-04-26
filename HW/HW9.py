# Task9:
# Given the entered number n, derive a pattern from numbers
# n could be in range 1 <= n <= 9.
# There are NO spaces at the end of lines.
# O NOT use methods of string type.
# You could solve this task for n > 9, but it would be task with * :)

# > Enter n: 2
#   1
# 1 2 1
#
# > Enter n: 5
#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1


# Solution9:
def print_number_pattern(n):
    for i in range(1, n + 1):
        print(" " * (2 * (n - i)), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()

n = int(input("Enter n: "))

print_number_pattern(n)
