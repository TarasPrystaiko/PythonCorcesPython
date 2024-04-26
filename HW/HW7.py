# Task7:
# Output a triangle of user-entered size.
# There are NO spaces at the end of lines.
# DO NOT use methods of string type.
# > Enter size of triangle: 5
#     *
#    **
#   ***
#  ****
# *****

# Solution7:
number_of_lines =  int(input("Enter size of triangle: "))
for line_number in range(1,number_of_lines+1):
    print(" " * (number_of_lines - line_number) + "*" * line_number)

