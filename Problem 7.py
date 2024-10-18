# Romain Tranchant
# CIS 103 : Fundamentals of programing
# Instructor: MD Ali
# Lab 6

# Problem 7: Dictionary of Word Frequencies
# Objective: Practice working with dictionaries and loops.
# Write a Python program that asks the user to input a sentence. The program should then create
# a dictionary where the keys are the words in the sentence, and the values are the frequencies of
# those words in the sentence. The program should print the dictionary.


# Define a function called
def frenquency_word():
# Ask the user to input a sentence
    input_sentence = input("Enter a sentence: ")
# Split the sentence into words
    sentence_words = input_sentence.split()
# Initialize an empty dictionary to store word frequencies
    freq_word_dict = {}
# Start a for loop tp go over each word in the list
    for word in sentence_words:
# If the word is already in the dictionary, increment its count
        if word in freq_word_dict:
            freq_word_dict[word] += 1
# If the word is not in the dictionary, add it with a count of 1
        else:
            freq_word_dict[word] = 1
# Print the dictionary using an f-string
    print(f"Word frequencies: {freq_word_dict}")

# Call the function
frenquency_word()