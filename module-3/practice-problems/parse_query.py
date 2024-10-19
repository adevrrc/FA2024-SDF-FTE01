"""
Description: 

In Internet programming, programmers receive parameters via a query string, 
which looks like a string with fields separated by the "&" character. Each 
field typically has a metadata part that identifies the data followed by an 
equals sign and then the data. An example of a query string is: 

first=Mike&last=Jones&id=mike1&password=hello

Read and parse a query string and output each field on a different line after
replacing the equal sign with a colon followed by a space. For example, for 
the preceding sample query string, the output should be:

first: Mike last: Jones id: mike1 password: hello

Input
query - part of an http request

Processing
- break apart query
- insert colon

Output
parsed query data - attribute and data separated by colon

Author: Damien Altenburg
Date: 2024-10-4
Usage: python parse_query.py
"""

query = input("Enter a query string: ")

# Break query into parts
attributes = query.split("&")

for attribute in attributes:
    attribute = attribute.replace("=", ": ")

    # Print without end line character
    print(attribute)
