# Romain Tranchant
# CIS 103 : Foundamentals of programing
# Instructor: MD Ali
# Lab 6

# Problem 5: Factorial Calculation
# Objective: Practice using loops and functions.
# Write a Python function called calculate_factorial that takes a positive integer as input and
# returns the factorial of that number. For example, if the input is 5, the function should return
# 120 (since 5! = 5 × 4 × 3 × 2 × 1).


# Define a function named factorial
def factorial():
# Ask the user to enter a positive number and convert it to an integer
        num1 = int(input("Enter a positive number:"))
# Check if the entered number is negative
        if num1 < 0:
# Raise an error if the number is negative
            raise ValueError("Input must be a positive number.")
# Check if the number is 0 or 1
        elif num1 == 0 or num1 == 1:
# Return 1 because the factorial of 0 and 1 is 1
            return 1
        else:
# Create a variable to store the factorial
            factor = 1
# Start a for loop from 2 to the input number
        for i in range(2, num1 + 1):
# Multiply the factor by each number in the loop
            factor *= i
# Return the entered number and its factorial
        return num1, factor

# Call the factorial function and store the result
num1, result = factorial()
# Print headers for the input and factorial
print("%12s%20s" % ("Input number", "Factorial number"))
# Print the input number and its factorial
print("%12s%20s" % (num1, result))
