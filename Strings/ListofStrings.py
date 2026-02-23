sentence = input("Enter a sentence: ")

# 1. Turn string into a list of words
words = sentence.split(" ") 
print("List of words is: ", words)

# 2. Reverse the list
words.reverse()
print("Reversed list of words is: ", words)

# 3. Join the list back into a string
new_sentence = " ".join(words)
print("New sentence is: ", new_sentence)