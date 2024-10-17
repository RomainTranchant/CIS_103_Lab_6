# Romain Tranchant
# CIS 103 : Foundamentals of programing
# Instructor: MD Ali
# Lab 6

# Objective: Practice using loops, conditionals, and functions.
# Write a Python function called is_prime that takes an integer as input and returns True if the
# number is prime and False otherwise. A prime number is a number greater than 1 that has no
# divisors other than 1 and itself.



def prime_checker():
    number = int(input("Enter a positive number:"))
    if number <= 1:
        print(f"{number} is not prime number")
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number")
            return False
    print(f"{number} is a prime number")
    return True

prime_checker()
