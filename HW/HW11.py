##The program has a string `sentences`.

# The string consists of sentences.
#
# A 'sentence' is a set of characters delimited by periods(. or ...) or the beginning of a line and a period.
#
# Return list with number of words in each sentence.
#
# A 'word' is a set of characters between two spaces or the beginning of a line and a space.
#
# DO NOT use regular expressions.
#
#Output
# sentences = "Hello all. Here's pretty cold and hot. Choose yourself."
# words_number -> [2, 5, 2]


def count_words(sentences):
    sentence_list = [sentence.strip() for sentence in sentences.split('.') if sentence.strip()]

    word_counts = []

    for sentence in sentence_list:
        words = sentence.split()

        word_counts.append(len(words))

    return word_counts


# Example usage:
sentences = "Hello all. Here's pretty cold and hot. Choose yourself."
result = count_words(sentences)
print(result)
