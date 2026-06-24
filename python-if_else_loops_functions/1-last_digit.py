#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Extract the last digit correctly for both positive and negative numbers
last_digit = abs(number) % 10

# Print the starting string prefix
print(f"Last digit of {number} is {last_digit}", end=" ")

# Evaluate the condition for the last digit
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

