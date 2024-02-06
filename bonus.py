'''
Define a string variable containing 
a sentence with at least 10 words.
'''
sentence = " My name is Maha and I am from Saudi Arabia "

'''
Define a string variable containing 
a word that appears in the sentence.
'''
word = "Maha"


# Print the length of the sentence.
print(len(sentence))

'''
Print the index of the first occurrence 
of the word in the sentence.
'''
print(sentence.index("Maha"))


'''
Print the number of times the word 
appears in the sentence.
'''
print(sentence.count("Maha"))


# Print the sentence in all uppercase letters.
print(sentence.upper())

# Print the sentence in all lowercase letters.
print(sentence.lower())


'''
Replace the word in the sentence 
with a new word of your choice.
'''
newWord = "Sara"
newSentence = sentence.replace(word, newWord)
print(newSentence)

# Print the last character of the sentence.
print(sentence[-1])