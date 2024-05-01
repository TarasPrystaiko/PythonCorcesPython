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
