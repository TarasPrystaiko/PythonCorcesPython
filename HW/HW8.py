# Task8:

# The user enters the minimum and maximum width of the diamond pattern.
# Print a "diamond" with given dimensions composed of '*' symbols.
# If the entered minimum width is greater than the maximum width, print a warning and terminate the program.
# If the difference between the maximum and minimum widths is not a multiple of 2, print a warning and terminate the program.
# There are NO spaces at the end of lines.
# DO NOT use methods of string type
#> Enter minimal width: 3
# > Enter maximal width: 5
#  ***
# *   *
#  ***
# > Enter minimal width: 1
# > Enter maximal width: 3
#  *
# * *
#  *
# > Enter minimal width: 2
# > Enter maximal width: 6
#   **
#  *  *
# *    *
#  *  *
#   **
# > Enter minimal width: 3
# > Enter maximal width: 9
#    ***
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    ***


# Solution8:

# Reading number of row
min = 2
row = int(input('Enter number of row: '))

# Upper part of hollow diamond
for i in range(min, row+1//2, 1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower part of hollow diamond
for i in range(row-1//2, min-1, -1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

