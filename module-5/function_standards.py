"""A script to demonstrate function standards and raising exceptions.

Example: 
    $ python function_standards.py
"""

__version__ = "0.11.2024"
__author__ = "Damien Altenburg"

def format_greeting(first_name: str, last_name: str, 
                    salutation="Hello", title="Mr.") -> str:
    """Returns a formatted greeting based on the specified person's
    first and last name.
    
    Args:
        first_name (str): The person's first name.
        last_name (str): The person's last name.
        salutation (str): The beginning phrase of the greeting. The
        default is "Hello".
        title (str): The person's title. The default is "Mr.".
    
    Returns:
        str: A formatted greeting based on the specified person's
        first and last name.

    Raises:
        TypeError: Raised when the first name or last name is not
        a string type.
        ValueError: Raised when the last name does not contain any
        non-whitespace characters.
    """
    if not isinstance(first_name, str):
        raise TypeError("The first name must be a string.")
    
    if not isinstance(last_name, str):
        raise TypeError("The last name must be a string.")
    
    if last_name.strip() == "":
        raise ValueError("The last name must contain characters.")

    first_name = first_name.strip()

    if first_name != "":
        first_name += " "

    return f"{salutation}, {title} {first_name} {last_name}"

def to_binary(decimal_number: int) -> str:
    binary_number = ""

    while decimal_number > 0:
        # The binary digit is the remainder of dividing by 2
        binary_digit = decimal_number % 2

        # Update the number to the the quotient
        decimal_number = int(decimal_number / 2)

        # Add the digit to the beginning of the string
        binary_number = str(binary_digit) + binary_number

    return binary_number

def main() -> None:

    greeting = format_greeting("Damien", "Altenburg")
    print(greeting)

if __name__ == "__main__":
    main()
