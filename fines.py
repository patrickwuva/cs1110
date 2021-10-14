'''
Name: Patrick Williamson
Date: September 29th, 2021
Computing id: upm8pb
'''


def fine(speed_limit, my_speed, zone=None):
    '''
    :param speed_limit: takes an int( speed limit)
    :param my_speed: take an int your speed
    :param zone: an optional str that makes the fine higher in special cases
    :return: using my_speed and speed_limit you can determine the fine and the fine is returned
    '''

    # lets set up if elif else statement for the fines

    # statement for reckless driving
    if my_speed >= speed_limit + 20:
        fine = 350

    # statement in a residential zone
    elif speed_limit < my_speed < speed_limit + 20 and zone == 'residential':
        fine = (my_speed - speed_limit) * 8 + 200

    # statement for ticket in a school or workzone
    elif speed_limit < my_speed < speed_limit + 20 and zone == 'work' or zone == 'school':
        fine = (my_speed - speed_limit) * 7

    # statement for ticket in a regualr zone
    elif speed_limit < my_speed < speed_limit + 20:
        fine = (my_speed - speed_limit) * 6

    # else statement which is when we are going under the speed limit
    elif speed_limit > my_speed:
        fine = 30
    else:
        fine = 0
    return fine


def demerits(speed_limit, my_speed):
    '''
    :param speed_limit: and int given for speed limit
    :param my_speed: and int given for current speed
    :return: using speed_limit and my_speed we can calucate the demarits based on how much higher my_speed is over the speed limit returing demerits
    '''

    # if else statements for demarits

    # if statement for + 20 over speed limit
    if my_speed >= speed_limit + 20:
        demerits = 6

    # if statement for 10-19 over speed limit
    elif speed_limit + 19 >= my_speed > speed_limit + 9:
        demerits = 4

    # if statement for 1-9 over speed limit
    elif speed_limit+ 9 >= my_speed > speed_limit:
        demerits = 3

    else:

        demerits = 0

    return demerits

