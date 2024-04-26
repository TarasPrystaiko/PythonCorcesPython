# Task6:
# User enters height and width of rectangle (integer numbers), and any symbol.
# Output a rectangle made up of the entered character of a given size.
# There are NO spaces at the end of lines.
#
# > Enter height of rectangular: 3
# > Enter width of rectangular: 6
# > Enter symbol to build rectangular with: ^
# ^^^^^^
# ^^^^^^
# ^^^^^^

# Solution6:
height = int(input("Enter the height of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
character = input("Enter the character to use: ")

for i in range(height):
    for j in range(width):
        print(character, end='')
    print()


