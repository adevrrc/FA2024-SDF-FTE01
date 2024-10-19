"""
Description: Write a program that multiplies by 2 all the elements of a List 
of floats.

Author: Damien Altenburg
Date: 2024-10-2
Usage: python number_doubler.py
"""

from pprint import pp
from random import randint

# Generate a list of random float values
temperatures = [randint(10, 100) / 10 for _ in range(10)]

# TESTING
print(temperatures)

# After reviewing the requirement again, I believe the problem is asking to
# update the list.
# for temperature in temperatures:
#    print(f"{temperature} >doubled>> {temperature * 2}")

# With a for loop
for index in range(0, len(temperatures)):
    temperatures[index] *= 2

# With a list comprehension
# temperatures = [temperature * 2 for temperature in temperatures]

pp(temperatures)
