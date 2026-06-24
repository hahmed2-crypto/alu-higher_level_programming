#!/usr/bin/python3
"""Module to print the last digit of a random number with conditions."""
import random
number = random.randint(-10000, 10000)

# Extract the last digit keeping the negative sign if the number is negative
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

# Base output string using standard string format
print("Last digit of {} is {}".format(number, last_digit), end=" ")

# Conditional evaluation based on the true value of the last digit
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

