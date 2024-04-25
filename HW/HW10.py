
user_input = input("Enter a string: ")
def is_palindrome_method1(s):
    s = s.strip().lower()
    reversed_s = s[::-1]
    return s == reversed_s


result_method1 = is_palindrome_method1(user_input)

print(result_method1)