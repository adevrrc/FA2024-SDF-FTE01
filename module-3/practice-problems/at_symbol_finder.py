"""
Description: Write a program that expects a word containing the @ character as 
an input. If the word does not contain an @ character, then your program should 
keep prompting the user for a word. When the user types in a word containing an 
@ character, the program should simply print the word and terminate.

Author: Damien Altenburg
Date: 2024-10-2
Usage: python at_symbol_finder.py
"""

word: str = "@"

while "@" in word:
    word = input("Enter a word: ")
