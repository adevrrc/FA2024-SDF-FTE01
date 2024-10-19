"""
Description: Write a program that takes a word representing a binary number 
(0s and 1s) as an input and converts it to its decimal representation; for 
instance, if the user inputs 101, then the output will be 5; you can assume 
that the input is guaranteed to contain only 0s and 1s.

Author: Damien Altenburg
Date: 2024-10-2
Usage: python binary_to_decimal.py
"""

binary_number: str = input("Enter binary number: ")

decimal_number: float = 0
exponent = len(binary_number)

for digit in binary_number:
    binary_digit: int = int(digit)

    exponent -= 1

    decimal_number += binary_digit * 2**exponent

print(f"The {binary_number} in decimal is {decimal_number}.")
