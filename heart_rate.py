"""
Author: Patrick Williamson
Computing id: upm8pb
Date: Wednesday September 22nd
"""

#the gellish2 formula
def gellish2(age):

    #lol I'm glad the error was because y'all forgot to square the formula i was like what in the world is going on
    hr_max = 191.5 - (0.007 * (age**2))

    #return it so we can use it a
    return hr_max


#now lets see if their heart is good
def in_target_range(hr, age):

    #call the gellish2 formula with the entered age which sets the 85% 65% window
    #since its in a T/F statement it will return either T or F
    return gellish2(age)*.85 >= hr >= gellish2(age)*.65


