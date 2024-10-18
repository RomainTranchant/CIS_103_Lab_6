# Romain Tranchant
# CIS 103 : Foundamentals of programing
# Instructor: MD Ali
# Lab 6

# Problem 6
# Objective: Practice using loops, conditionals, and functions.
# Write a Python function called is_prime that takes an integer as input and returns True if the
# number is prime and False otherwise. A prime number is a number greater than 1 that has no
# divisors other than 1 and itself.


# Define a function named prime_checker
def prime_checker():
# Ask the user to enter a positive number and convert it to an integer
    number = int(input("Enter a positive number:"))
# Check if the input number is less than or equal to 1
    if number <= 1:
# Print that the number is not prime
        print(f"{number} is not a prime number")
# Return False indicating the number is not prime
        return False
# Loop from 2 to the square root of the input number
    for i in range(2, int(number ** 0.5) + 1):
# Check if the input number is divisible by i
        if number % i == 0:
# Print that the number is not prime
            print(f"{number} is not a prime number")
# Return False indicating the number is not prime
            return False
# Print that the number is a prime number
    print(f"{number} is a prime number")
# Return True indicating the number is prime
    return True

# Call the prime_checker function
prime_checker()
