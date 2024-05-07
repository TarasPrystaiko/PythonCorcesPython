#There's a string with email address.

# Print True if the string is a valid address, otherwise False.
#
# Valid address is considered:
#
# - '@' comes before '.'
#
# - the string does not start with '@' and does not end with '.'
#
# - symbols except '@' and '.' should be letters and decimal digits
#
# - containing only one '@' and only one '.'
#
# Specify strings for testing your code in comments.
#
# DO NOT use regular expressions.
#
#Output
# email = "aaa@bbb.ccc"  # True
def is_valid_email(email):
    dog_count = 0
    dot_count = 0

    for char in email:
        if char == '@':
            dog_count += 1
        elif char == '.':
            dot_count += 1
        elif not char.isalnum():
            if char != '@' and char != '.':
                return False


    if dog_count == 1 and dot_count == 1 and email[0] != '@' and email[-1] != '.':
        return True
    else:
        return False


#cases
email1 = "user@example.com"
email2 = "user@@example.com"
email3 = "@example.com"
email4 = "user@example"
email5 = "user@example."

print(is_valid_email(email1))
print(is_valid_email(email2))
print(is_valid_email(email3))
print(is_valid_email(email4))
print(is_valid_email(email5))



# def main():
#     while True:
#         email = input("Enter an email address: ")
#
#         if is_valid_email(email):
#             print("Valid email address.")
#             break
#         else:
#             print("Invalid email address. Try again.")
#
#
# main()

# email = ""
# result = None
#
# if email[0] == '@':
#     result = False
# elif email[-1] == '.':
#     result = False
# else:
#     result = True
#     print(result)
