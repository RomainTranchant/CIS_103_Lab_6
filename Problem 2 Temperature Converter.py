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

# Define the temperature converter function
def temperature_converter():

# Start an infinite loop to allow multiple conversions
    while True:
        try:

# Ask the user to enter the temperature and convert it to a float number
            temperature = float(input("Enter the temperature: "))

# Ask the user to enter the unit of temperature and convert it to uppercase
            unit = input("Enter the unit of temperature, 'C' for Celsius, 'F' for Fahrenheit: ").upper()

# If the input unit is Celsius, convert the temperature to Fahrenheit and store it in the ftc variable
            if unit == 'C':
                ftc = (temperature * 9 / 5) + 32

# Print the temperature in Celsius
                print(f"Temperature in Celsius is {temperature:.2f} degrees")

# Print the converted temperature in Fahrenheit
                print(f"Temperature in Fahrenheit is {ftc:.2f} degrees")

# If the input unit is Fahrenheit, convert it to Celsius and store it in the ctf variable
            elif unit == 'F':
                ctf = (temperature - 32) * 5 / 9

# Print the temperature in Fahrenheit
                print(f"Temperature in Fahrenheit is {temperature:.2f} degrees")

# Print the converted temperature in Celsius
                print(f"Temperature in Celsius is {ctf:.2f} degrees")

# If the unit is neither 'C' nor 'F', raise a ValueError
            else:
                raise ValueError("Invalid unit, it must be 'C' or 'F'.")

# Handle any ValueError exceptions that occur
        except ValueError as error:
# Print the error message
            print(error)


# Call the temperature converter function
temperature_converter()
