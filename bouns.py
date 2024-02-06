#Define a string variable containing a sentence with at least 10 words.
favorite_car:str = "Speed Luxury Performance Design Comfort Innovation Power Efficiency Reliability Elegance"
word_to_find = "Design"
word_to_count = "Design"
#Define a string variable containing a word that appears in the sentence.
the_word = "Design"

#Print the length of the sentence.
length = len(favorite_car)
print(length)

#Print the index of the first occurrence of the word in the sentence.
index = favorite_car.find(word_to_find)

print(index)

#Print the number of times the word appears in the sentence.
count = favorite_car.count(word_to_count)

print(count)

#Print the sentence in all uppercase letters.
print(favorite_car.upper())

#Print the sentence in all lowercase letters.
print(favorite_car.lower())

#Replace the word in the sentence with a new word of your choice.
old_word = "Design"
new_word = "Aerodynamics"
updated_sentence = favorite_car.replace(old_word, new_word)

print(updated_sentence)

#Print the last character of the sentence.
print(favorite_car)

#Print the last character of the sentence.
print(favorite_car[-1])