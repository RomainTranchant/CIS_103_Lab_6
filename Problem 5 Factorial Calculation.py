# Romain Tranchant
# CIS 103 : Foundamentals of programing
# Instructor: MD Ali
# Lab 6

# Problem 5: Factorial Calculation
# Objective: Practice using loops and functions.
# Write a Python function called calculate_factorial that takes a positive integer as input and
# returns the factorial of that number. For example, if the input is 5, the function should return
# 120 (since 5! = 5 × 4 × 3 × 2 × 1).


def factorial():
        num1 = int(input("Enter a positive number:"))
        if num1 < 0:
            raise ValueError("Input must be a positive number.")
        elif num1 == 0 or num1 == 1:
            return 1
        else:
            factor = 1
            for i in range(2, num1 + 1):
                factor *= i
            return num1, factor

# Example usage:
num1, result = factorial()
print("%12s%20s" % ("Input number", "Factorial number"))
print("%12s%20s" % (num1, result))




