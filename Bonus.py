sentence:str="A programming language is a set of symbols,grammars and rules with help of which one is able to translate algorithms to programs that will be executed by the computer"
word:str="programming"
print(len(sentence))
print(sentence.index(word))
print(sentence.count(word))
print(sentence.upper())
print(sentence.lower())
word1= "machine"
print(sentence.replace(word, word1))
print(sentence[-1])