# - Define a string variable containing a sentence with at least 10 words.
sentance:str = "Tuwaiq Academy provides a great Python web development bootcamp for graduates"

# - Define a string variable containing a word that appears in the sentence.
word:str = "great"

# - Print the length of the sentence.
print("Length of the sentence:",len(sentance))

# - Print the index of the first occurrence of the word in the sentence.
print("First index of the first occurance of the word in the sentaence:",sentance.index(word))

# - Print the number of times the word appears in the sentence.
print("Number of times the word appears in the sentence:",sentance.count(word))

# - Print the sentence in all uppercase letters.
print("Sentence in all uppercase letters:",sentance.upper())

# - Print the sentence in all lowercase letters.
print("Sentence in all lowercase letters:",sentance.lower())

# - Replace the word in the sentence with a new word of your choice.
print("Replace the word in the sentence with a new word:", sentance.replace(word ,"fantastic"))

# - Print the last character of the sentence.
print("last character of the sentence:", sentance[-1])



