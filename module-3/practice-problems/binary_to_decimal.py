"""
Description: Write a program that takes a word representing a binary number 
(0s and 1s) as an input and converts it to its decimal representation; for 
instance, if the user inputs 101, then the output will be 5; you can assume 
that the input is guaranteed to contain only 0s and 1s.

Author: Damien Altenburg
Date: 2024-10-2
Usage: python binary_to_decimal.py
"""

def to_decimal(binary_number: str) -> float:
    """Returns the decimal version of the binary number.
    
    Args:
        binary_number (str) - The binary number to convert to a decimal.
        
    Returns:
        float - The decimal version of the binary number.
    """
    decimal_number: float = 0
    exponent = len(binary_number)

    for digit in binary_number:
        binary_digit: int = int(digit)

        exponent -= 1

        decimal_number += binary_digit * 2**exponent

    return decimal_number

def main() -> None:
    """The main function of the program."""
    # Get the input
    binary_number: str = input("Enter binary number: ")

    # Do the conversion
    decimal_number = to_decimal(binary_number)

    # Output the result
    print(f"The {binary_number} in decimal is {decimal_number}.")

# python script.py
# from binary_to_decimal import to_decimal
if __name__ == "__main__":
    main()

print(__name__)
