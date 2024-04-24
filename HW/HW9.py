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
