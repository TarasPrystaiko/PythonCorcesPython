users = [
    {'name': 'Luarvik L. Luarvik', 'age': 17},
    {'name': 'Olaf Andvarafors', 'age': 18},
    {'name': 'Brun Du Barnstokr', 'age': 19}
]

names_18_or_older = []

for user in users:
    if user['age'] >= 18:
        names_18_or_older.append(user['name'])

# Output the list of names of users who are 18 or older
print(names_18_or_older)
