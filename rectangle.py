'''
Author: Patrick Williamson
Computing id: upm8pb
Date September 9th
'''


#lets get the input
character = input('Enter a character: ')
width = int(input('Width: '))

#now lets print the output by multiplying the character by the width

print(character*width)

#since its a 3x3 we can use this formula to get the middle row
print(character+(" "*(width-2))+character)

#print the last row and let the user know some information
print(character*width)
print('"'+character+'"' +' rectangle has a width of ' + str(width))

