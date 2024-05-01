def print_words_with_double_o(string):
    words = string.split()

    for word in words:
        count_o = word.lower().count('o')
        if count_o == 2:

            print(word.title())

string = "This tool is cool. But that owl is awful. MAGIC TOOLS Ltd."

print_words_with_double_o(string)
