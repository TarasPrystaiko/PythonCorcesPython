#Task4:
#Request two integer numbers from user.
# Output on one line expression with sum of numbers, and on another line - expression with product of numbers:
# > Enter a: 3
# > Enter b: 5
# 3 + 5 = 8
# 3 * 5 = 15

# Solution4:
num1 = int(input("Enter first integer number: "))
num2 = int(input("Enter second integer number: "))

result1 = num1 + num2
result2 = num1 * num2

print(f" {num1} + {num2} = {result1}")
print(f" {num1} * {num2} = {result2}")