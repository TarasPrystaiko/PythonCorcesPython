height = int(input("Enter the height of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
character = input("Enter the character to use: ")

for i in range(height):
    for j in range(width):
        print(character, end='')
    print()
