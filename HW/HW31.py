def extract_hrefs_string_methods(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    hrefs = []
    start = 0

    while True:
        start = content.find('<a ', start)
        if start == -1:
            break
        start_href = content.find('href="', start) + len('href="')
        end_href = content.find('"', start_href)
        href = content[start_href:end_href]
        hrefs.append(href)
        start = end_href

    return hrefs

import re

def extract_hrefs_regex(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    hrefs = re.findall(r'<a [^>]*href="([^"]*)"', content)
    return hrefs

file_path = '/mnt/data/wiki_page.txt'
hrefs_string_methods = extract_hrefs_string_methods(file_path)
print("Using string methods:", hrefs_string_methods)

hrefs_regex = extract_hrefs_regex(file_path)
print("Using regex:", hrefs_regex)
