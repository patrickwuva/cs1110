"""
computing id: upm8pb
date: 9/15/21
name: Patrick Williamson
"""

# let's get the info we need to calculate their age
number = int(input('Pick a number between 1 and 10: '))
year = int(input("If you've already had a birthday this year, enter 1771. Otherwise, enter 1770: "))
yearOfBirth = int(input("Enter the year that you were born: "))

# lets calculate the magic number and age
magicNumber = (number*2+5) * 50
magicNumber = magicNumber + year
magicNumber = magicNumber - yearOfBirth
age = magicNumber%100

# lets output the data and make the user happy
print('The magic number is ' + '"'+ str(magicNumber) + '"' + ". That means you are "+ str(age) + "!")