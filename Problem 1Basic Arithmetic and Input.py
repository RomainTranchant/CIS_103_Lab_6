# Romain Tranchant
# CIS 103 : Foundamentals of programing
# Instructor: MD Ali
# Lab 6

# Problem 1: Basic Arithmetic and Input
# Objective: Practice using basic arithmetic operations and user input.
# Write a Python program that asks the user to enter two numbers. The program should then
# calculate and print the sum, difference, product, and quotient (division result) of the two
# numbers.

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero!."


def main():
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '5':
            print("exiting, thank you!")
            break

        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()

