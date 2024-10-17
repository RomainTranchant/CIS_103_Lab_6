# Romain Tranchant
# CIS 103 : Foundamentals of programing
# Instructor: MD Ali
# Lab 6

# Objective: Practice string manipulation and loops.
# Write a Python function called reverse_string that takes a string as input and returns the string
# reversed. For example, if the input is "hello", the function should return "olleh".

# Create a reverse_string function using the_string as a parameter
def reverse_string(the_string):

# Print the original string
    print(f"The original string is: {the_string}")
  
# Create an empty string to get the reversed string 
    reversed_string = ""
  
# Use a for loop to go through the original string and slice to reverse the original string
    for char in the_string[::-1]:

# Append each character to the reversed_string and print the reversed string
        reversed_string += char
    print(f"The reversed string is: {reversed_string}")

# Define the original string
the_string = "Hello"

# Call the function using the string as a parameter
reverse_string(the_string)
