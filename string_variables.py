# Point 1 "Define a string variable containing a sentence with at least 10 words."
sentence = "Python is high level programming language it is a powerful and used for various purposes"

# Point 2 "Define a string variable containing a word that appears in the sentence."
word = "powerful"

# Point 3 "Print the length of the sentence."
print("Length of the sentence:", len(sentence))

# Point 4 "Print the index of the first occurrence of the word in the sentence."
print("Index of the first occurrence of the word:", sentence.index(word))

# Point 5 "Print the number of times the word appears in the sentence."
print("Number of times the word appears:", sentence.count(word))

# Point 6 "Print the sentence in all uppercase letters."
print("Sentence in uppercase:", sentence.upper())

# Point 7 "Print the sentence in all lowercase letters."
print("Sentence in lowercase:", sentence.lower())

# Point 8 "Replace the word in the sentence with a new word of your choice."
new_word = "well built"
new_sentence = sentence.replace(word, new_word)
print("New sentence:", new_sentence)

# Point 9 "Print the last character of the sentence."
print("Last character of the sentence:", sentence[-1])
