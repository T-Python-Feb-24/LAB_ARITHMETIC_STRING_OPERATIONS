# Define a string variable containing a sentence with at least 10 words.
x = "Kingdom of Saudi Arabia"

# Define a string variable containing a word that appears in the sentence.
y = "Kingdom"

# Print the length of the sentence.
print(len(x))

# Print the index of the first occurrence of the word in the sentence.
print(x.find(y))

# Print the number of times the word appears in the sentence.
print(x.count(y))

# Print the sentence in all uppercase letters.
print(x.upper())

# Print the sentence in all lowercase letters.
print(x.lower())

# Replace the word in the sentence with a new word of your choice.
z = x.replace(y, "Country")
print(z)

# Print the last character of the sentence.
print(x[-1])