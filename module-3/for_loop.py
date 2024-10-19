"""
Description: A script to demonstrate the for loop.
Author: Damien Altenburg
Date: 2024-9-26
Usage: python for_loop.py
"""
THRESHOLD: int = 23
temperatures: list[int] = [19, 23, 24, 18, 24, 29, 35, 35, 23, 27]
number_of_temperatures_below_threshold: int = 0

# For each element in a list
for temperature in temperatures:
    if temperature < THRESHOLD:
        number_of_temperatures_below_threshold += 1

print(f"There are {number_of_temperatures_below_threshold} "
      f"temperatures below {THRESHOLD}.")

uppercase_letter_count: int = 0
lowercase_letter_count: int = 0
whitespace_character_count: int = 0

# For each character in a string
for character in "Damien Altenburg":
    if character.islower():
        lowercase_letter_count += 1
    elif character.isupper():
        uppercase_letter_count += 1
    else:
        whitespace_character_count += 1

print(f"Uppercase: {uppercase_letter_count}")
print(f"Lowercase: {lowercase_letter_count}")
print(f"Whitespace: {whitespace_character_count}")

hockey_teams: dict[str, str] = {
    "winnipeg": "jets",
    "calgary": "flames",
    "edmonton": "oilers"
}

# For each element in a dictionary
for key in hockey_teams:
    print(f"{key.upper()} -> {hockey_teams[key].title()}")

# For each element in a list of integer values generated by range()
for number in range(1, 10):
    print(number)

for number in range(2, 40, 2):
    print(number)

for number in range(0, -10, -1):
    print(number)
