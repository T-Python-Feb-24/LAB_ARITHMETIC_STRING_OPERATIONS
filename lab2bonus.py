#Define a string variable containing a sentence with at least 10 words.
sentence ="Hello I am Rayan Alshehri I am 21 and this is my solution"

#Define a string variable containing a word that appears in the sentence.
word="I am"

#Print the length of the sentence.
print("The length of the sentence",len(sentence))

#Print the index of the first occurrence of the word in the sentence.
print("the index of first occurrence: ",sentence.index(word))

#Print the number of times the word appears in the sentence.
print("The number of times: ",sentence.count(word))

#Print the sentence in all uppercase letters.
print("in uppercase: ",sentence.upper())

#Print the sentence in all lowercase letters.
print("in lowercase: ",sentence.lower())

#Replace the word in the sentence with a new word of your choice.
print("after replace: ",sentence.replace(word,"Hi"))

#Print the last character of the sentence.
print("The last character: ",sentence[-1])

'''
The output is:

The length of the sentence 57
the index of first occurrence:  6
The number of times:  2
in uppercase:  HELLO I AM RAYAN ALSHEHRI I AM 21 AND THIS IS MY SOLUTION
in lowercase:  hello i am rayan alshehri i am 21 and this is my solution
after replace:  Hello Hi Rayan Alshehri Hi 21 and this is my solution
The last character:  n
'''