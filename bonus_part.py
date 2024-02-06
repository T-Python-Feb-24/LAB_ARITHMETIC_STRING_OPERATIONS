# String with at least 10 words
qoute = "Keep doing your best every day and if no one is proud of you, be proud of yourself."

# Word appears in the qoute
word = "proud"

# Print the length of the sentence.
print(len(qoute))

# Print the index of the first occurrence of the word in the sentence.
print(qoute.find(word))

# Print #of times the word appears in the sentence.
print(qoute.count(word))

# Print the sentence in all uppercase letters.
print(qoute.upper())

# Print the sentence in all lowercase letters.
print(qoute.lower())

# Replace the word in the sentence with a new word
print(qoute.replace(word, "prideful"))

#Print the last character of the sentence.
print(qoute[-1])