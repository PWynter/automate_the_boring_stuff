#! python3
# phoneAndEmail.py - Finds phone numbers and email addreses on the clipboard.

import pyperclip, re

phoneNumRegex = re.compile(r"""(
	(\d{3}|\(\d{3}\))?        #area code
	(\s|-|\.)?                #seperator
	(\d{3})                   #first 3 digits
	(\s|-|\.)                 #separator
	(\d{4})                   #last 4 digits
	(\s*(ext|x|ext.)s*(\d{2,5}))?
	)""", re.VERBOSE) 

# TODO: Create email regex
emailRegex = re.compile(r"""(
	[a-zA-Z0-9.%+-]+		 # username (character class[] means can contain) 
	@						 # @ symbol
	[a-zA-Z0-9.-]			 # domain name
	(\.[a-zA-Z]{2,4})
	)""", re.VERBOSE)

#TODO: Find matches in clipboard text.

#TODO: Copy results to the clipboard.











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
