import re

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d") 
mo = phoneNumRegex.search("My number is 415-555-4242.")
print(f"Phone number found: {mo.group()}")

""" Review of Regular Expression Matching
While there are several steps to using regular expressions in Python, each
step is fairly simple.

1. Import the regex module with import re.
2. Create a Regex object with the re.compile() function. (Remember to use a
raw string.)
3. Pass the string you want to search into the Regex object’s search() method.
This returns a Match object.
4. Call the Match object’s group() method to return a string of the actual
matched text."""
