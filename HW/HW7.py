number_of_lines =  int(input("Enter size of triangle: "))
for line_number in range(1,number_of_lines+1):
    print(" " * (number_of_lines - line_number) + "*" * line_number)

