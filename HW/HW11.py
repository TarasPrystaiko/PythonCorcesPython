def count_words(sentences):
    # Split the string into individual sentences
    sentence_list = [sentence.strip() for sentence in sentences.split('.') if sentence.strip()]

    # Initialize an empty list to store the number of words in each sentence
    word_counts = []

    # Iterate over each sentence
    for sentence in sentence_list:
        # Split the sentence into words
        words = sentence.split()

        # Count the number of words in the sentence and append to the word_counts list
        word_counts.append(len(words))

    return word_counts


# Example usage:
sentences = "Hello all. Here's pretty cold and hot. Choose yourself."
result = count_words(sentences)
print(result)  # Output: [2, 5, 2]
