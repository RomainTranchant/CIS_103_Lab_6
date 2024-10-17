# Romain Tranchant
# CIS 103 : Foundamentals of programing
# Instructor: MD Ali
# Lab 6

# Problem 3: List Manipulation
# Objective: Practice working with lists and loops.
# Write a Python program that asks the user to input a list of numbers separated by commas. The
# program should then convert the input into a list of integers and print the following:
# - The maximum number in the list
# - The minimum number in the list
# - The sum of all numbers in the list
# - The list sorted in ascending order

# Create empty list to store the numbers
the_list = []

# Define a function to create and process the list
def create_list():

# Start an infinite loop to continuously ask for user input
    while True:
        
# Ask the user for input and convert it to uppercase 
        user_input = (input("Enter a number, press 'Q' to exit:")).upper()

# Check if the user wants to exit the loop by writing 'Q' and exit the
# loop through the break statement
        if user_input == "Q":
            break  

# Try to convert the input string to a float
        try:
            str_to_num = float(user_input)
# Append the converted number to the list
            the_list.append(str_to_num)
        except ValueError:
# Handle the case where the input cannot be converted to a float and print
# an "Inbvalid input" message
            print("invalid input")  

# Print the current state of the list
        print(f"The list is: {the_list}")

# Calculate the maximum number in the list
        the_list_max = max(the_list)
# Calculate the minimum number in the list
        the_list_min = min(the_list)
# Calculate the sum of all numbers in the list
        the_list_sum = sum(the_list)
# Sort the list in ascending order
        the_list_sort = sorted(the_list)

# Print the maximum number found in the list
        print(f"The max number is: {the_list_max}")
# Print the minimum number found in the list
        print(f"The min number is: {the_list_min}")
# Print the sum of the numbers in the list
        print(f"The list sum is: {the_list_sum}")
# Print the sorted version of the list
        print(f"The sorted list is: {the_list_sort}")


# Call the create_list function
create_list()
