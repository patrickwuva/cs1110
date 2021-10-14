'''
Author: Patrick Williamson
Computing id upm8pb
Date September 7th, 2021

'''

# Get input input
# also make sure input is formatted properly for later math
player = input('What player would you like to calculate statistics for? ')
team = input('What team was the opponent in the game you would like to calculate statistic for? ')
threes = int(input("How many 3's did " + player + " attempt this game? "))
threesMade = int(input("How many 3's did " + player + " make this game? "))
twos = int(input("How many 2's did " + player + " attempt this game? "))
twosMade = int(input("How many 2's did " + player + " make this game? "))
freeThrows = int(input("How many free throws did " + player + " attempt this game? "))
freeThrowsMade = int(input("How many free throws did " + player + " make this game? "))

# do the math for field goals
fgp = (float(threesMade) + float(twosMade)) / (float(threes) + float(twos))

# now I have to formatt it so it looks pretty in the output
fgp = fgp * 100
ftp = float(freeThrowsMade) / float(freeThrows)
ftp = ftp * 100

# final output
print(player+' had a '+str(fgp)+"% field goal percentage and a "+str(ftp)+"% free throw percentage")
print(player +" scored " + str((threesMade*3+twosMade*2+freeThrowsMade)) +" points against " + team + '. Wahoowa!')



'''
I used google thinking moving the decimal place over was going to be hard
but it was easy
https://appdividend.com/2021/06/16/how-to-calculate-a-percentage-in-python/
'''