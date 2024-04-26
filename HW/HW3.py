# Task3
#Create list of 3 countries names.
#Create dictionary of 3 key-value pairs.
#Key should be country name from the list and value should be string with its capital.
# Ukraine: Kyiv
# Spain: Madrid
# Italy: Rome



# Solution3:
contries_list = ['Ukraine', 'Spain', 'Italy']

dictionary_output = {contries_list[0]: 'Kyiv', contries_list[1]: 'Madrid', contries_list[2]: 'Rome'}

for key, value in dictionary_output.items():
    print(f"{key}: {value}")
