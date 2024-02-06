#Define a string variable containing a sentence with at least 10 words.
phrase:str = 'Hello my name is Hammam'

#Define a string variable containing a word that appears in the sentence
word_in_the_sentence:str = 'Hammam'

#Print the length of the sentence.
print(len(phrase))

#Print the index of the first occurrence of the word in the sentence.
print(word_in_the_sentence[0])

#Print the number of times the word appears in the sentence.
print(phrase.count(word_in_the_sentence))

#Print the sentence in all uppercase letters
print(phrase.upper())

#Print the sentence in all lowercase letters.
print(phrase.lower())

#Replace the word in the sentence with a new word of your choice
word_in_the_sentence = 'randomly'

#Print the last character of the sentence.
print(phrase[-1])
