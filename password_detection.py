#! python3
#password_detction- checks if passwords are strong enough.
import re

print("""\nCreate a password with:\n
One or more lowercase letters
One or more uppercase
One or more digits
Minimum of 8 characters long""")

#create pattern
passwordRegex = re.compile(r"""
^ #match start
(?=.*?[A-Z]) #atleast one uppercase letter
(?=.*?[a-z]) #atleast one lowercase letter
(?=.*?[0-9]) #atleast one number
(?=.*?[#?!@$%^&*-]) #atleast one special character
.{8,} #minimum 8 characters
$ #matchend
""",re.VERBOSE)

#ask and save user password
password = str(input(" \nCreate a password: "))

match = passwordRegex.fullmatch(password)

#group returns string of matched objects

if match:
	print("Great code")
else:
	print("Your code is weak")



""" Strong Password Detection
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple
regex patterns to validate its strength. """



