
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
#
# def main():
#     while True:
#         # Get user input
#         email = input("Enter an email address: ")
#
#         # Call the function and check if the email is valid
#         if is_valid_email(email):
#             print("Valid email address.")
#             break
#         else:
#             print("Invalid email address. Try again.")
#
#
# main()