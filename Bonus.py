# Define a string variable containing a sentence with at least 10 words.
sentence: str = "Python is a popular programming language. It was created by Guido van Rossum, and released in 1991."

# Define a string variable containing a word that appears in the sentence.
pattern = "popular"

# Print the length of the sentence.
print(f"The length of sentence is {len(sentence)}", end="\n\n")

# Print the index of the first occurrence of the word in the sentence.
print(f"The index of the first \
occurrence of word \"{pattern}\" \
in the sentence is {sentence.index(pattern)}", end="\n\n")

# Print the number of times the word appears in the sentence.
print(f"Times the word appears is {sentence.count(pattern)} times", end="\n\n")

# Print the sentence in all uppercase letters.
print(sentence.upper())

# Print the sentence in all lowercase letters.
print(sentence.lower(), end="\n\n")

# Replace the word in the sentence with a new word of your choice.
print(sentence.replace(pattern, "unpopular"))

# Print the last character of the sentence.
print(sentence[-1])
