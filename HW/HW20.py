longest_line_length = 0
longest_line = ""

with open("your_file.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        line_length = len(line)

        if line_length >= longest_line_length:
            longest_line = line
            longest_line_length = line_length

# Print the longest line found
print(longest_line)
