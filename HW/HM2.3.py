# from pprint import pprint
#
# Dictionary_output = {'Ukraine': 'Kyiv', 'Spain': 'Madrid', 'Italy': 'Rome'}
#
# pprint(Dictionary_output, width=1)

from pprint import pprint

Dictionary_output = {'Ukraine': 'Kyiv', 'Spain': 'Madrid', 'Italy': 'Rome'}

for key, value in Dictionary_output.items():
        print(key, ":", value)