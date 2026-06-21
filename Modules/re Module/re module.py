# The re module in Python is used for working with Regular Expressions (Regex). A regular expression
#  is a special sequence of characters that helps you match, find, or replace specific patterns in
#  text (like looking for an email address, a phone number, or making sure a user input fits a
#  specific format).

# re.search(pattern, string): Scans through a string looking for the first location where the regex pattern matches. It returns a match object if found, or None if not.

# re.match(pattern, string): Checks for a match only at the very beginning of the string. If the pattern isn't at the start, it returns None.

# re.fullmatch(pattern, string): Checks if the entire string perfectly matches the pattern from start to finish.

# re.findall(pattern, string): Finds all matches in the string and returns them as a list of strings.

# re.sub(pattern, replacement, string): Finds matches and replaces them with a new string (like a smart "Find and Replace").

import re

notes = "The patient was diagnosed with Type 2 Diabetes last year."

# We look for the exact word "Diabetes"
if re.search("Diabetes", notes):
    print("Found it!")
else:
    print("Not found.")

#--------------------------------------------------------------


import re

id_1 = "p1002"
id_2 = "pABC"

pattern = r"p\d+"  # Means: a 'p' followed by one or more numbers

print(re.fullmatch(pattern, id_1))  # This MATCHES (Returns a match object)
print(re.fullmatch(pattern, id_2))  # This FAILS (Returns None because 'ABC' are not numbers)

#-------------------------------------------------------------------


import re

id_1 = "P1001"  # Uses a Capital P
pattern = r"p\d+"

# Without the flag, this fails because 'P' is capital:
print(re.fullmatch(pattern, id_1))  # Result: None

# With the flag, it ignores the case and works perfectly!
print(re.fullmatch(pattern, id_1, re.IGNORECASE))  # Result: Match object!