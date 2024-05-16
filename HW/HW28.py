import re


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$'

    match = re.match(pattern, email)

    if match and email.count('@') == 1:
        return True
    else:
        return False


email = "aaa@bbb.ccc"
email1 = "aaa@bbbccc"
email2 = "aaabbb.ccc"
email3 = "aaabbbccc"


print(is_valid_email(email))
print(is_valid_email(email1))
print(is_valid_email(email2))
print(is_valid_email(email3))
