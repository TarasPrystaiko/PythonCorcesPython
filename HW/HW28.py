import re


def is_valid_email(email):
    # Regular expression pattern for validating email address
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$'

    # Match the email address with the pattern
    match = re.match(pattern, email)

    # If there's a match and there's only one '@' symbol, return True
    if match and email.count('@') == 1:
        return True
    else:
        return False


# Example usage
email = "aaa@bbb.ccc"
print(is_valid_email(email))  # Output: True
