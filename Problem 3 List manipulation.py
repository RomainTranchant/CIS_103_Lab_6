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

the_list = [1, 8, 9, 26, 2, 9859, 5, 48, 88, 99, 53, 69]
print(f"The list is: {the_list}")
the_list_max = max(the_list)
the_list_min = min(the_list)
the_list_sum = sum(the_list)
the_list_sort = sorted(the_list)

print(f"The max number is: {the_list_max}")
print(f"The min number is: {the_list_min}")
print(f"The list sum is: {the_list_sum}")
print(f"The sorted list is: {the_list_sort}")
