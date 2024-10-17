# Romain Tranchant
# CIS 103 : Foundamentals of programing
# Instructor: MD Ali
# Lab 6

# Problem 2: Temperature Converter
# Objective: Practice using conditionals and functions.
# Write a Python function called convert_temperature that takes two arguments: a temperature
# and a unit ('C' for Celsius or 'F' for Fahrenheit). The function should convert the temperature to
# the other unit and return the result. For example, if the input is 32 and 'F', the function should
# return 0 (the temperature in Celsius).


def temperature_converter():
    while True:
        try:
            temperature = float(input("Enter the temperature: "))
            unit = input("Enter the unit of temperature, 'C' for Celsius, 'F' for Fahrenheit: ").upper()
            if unit == 'C':
                ftc = (temperature * 9/5) + 32
                print(f"Temperature in Celsius is {temperature:.2f} degrees")
                print(f"Temperature in Fahrenheit is {ftc:.2f} degrees")
            elif unit == 'F':
                ctf = (temperature - 32) * 5/9
                print(f"Temperature in Fahrenheit is {temperature:.2f} degrees")
                print(f"Temperature in Celsius is {ctf:.2f} degrees")
            else:
                raise ValueError("Invalid unit, it must be 'C' or 'F'.")
        except ValueError as error:
            print(error)


temperature_converter()


