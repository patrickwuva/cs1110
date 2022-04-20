import pygame
import random
import gamebox

# variables used throught the code
saved_score = 0
score = 0
width = 500
height = 600
r_x = width / 2
camera = gamebox.Camera(width, height)
floor_left = []
floor_right = []
player_vel = 5
box = gamebox.from_color(250, 50, 'red', 20, 20)
bottom = gamebox.from_color(250,600,'green',600,20)
block_vel = -1

def generate_floors(num,floor_location=300):
    '''
    we want to be able to generate the floors and gaps. using random()
    :param num: the numeber of blocks we want to make
    :param floor_location: optional param default is y = 300
    :return: nothing but we now have updated the left_floor and right_floor list with num amount of blocks
    '''
    # getting the block speed
    global block_vel

    # the for loop that creates the flor
    for i in range(num):

        # making the size of the left floor
        left_size = random.randint(0, 280)

        # making the size of the right block which is the left floor minus 40 to create an equal gap in every floor
        right_size = (600 - left_size - 40)

        # using the previous variables to create the floors
        floor_left.append(gamebox.from_color(((600 - right_size - 40) / 2), floor_location, 'white', left_size, 20))
        floor_right.append(gamebox.from_color(((600 + left_size + 40) / 2), floor_location, 'white', right_size, 20))
        floor_location +=50

        # setting the speed for the floors (it is important to use the global var block_velocity or the speed won't adjust as it increases throught the game
        for floor in floor_left:
            floor.speedy = block_vel

        for floor in floor_right:
            floor.speedy = block_vel


# generating the floors
generate_floors(10)

def display():
    """
    the display funciton that sets up the game
    :return: nothing
    """
    # clear the camera first
    camera.clear('black')

    # for loop that draws the floors
    for floor in floor_left:
        camera.draw(floor)
    for floor in floor_right:
        camera.draw(floor)

    # draw the box and the score
    camera.draw(box)
    camera.draw(('Score: ' + str(score)), 30, "red", width - 60, 10)
    camera.display()
    box.move_speed()


def get_score():
    """
    checking to see if the player falls through the gap
    :return: updated score
    """
    global block_vel
    global score
    global saved_score
    global player_vel

    # running a loop checking to see if the box is above the current box
    for floor in floor_left:
        if box.y <= floor.y:

            # updating the score to be the index of the floor, which ends up being the corrct score
            score = floor_left.index(floor)

            # loop that checks to see if we fall through another gab
            if saved_score != score:
                saved_score = score

                # generate another set of floors at the location of the last floor in the previous set of generated
                # floors minus the proper gap
                generate_floors(5,floor_left[len(floor_left)-1].y+50)

                # we need to create a max speed so the game isn't impossible. once it hits this speed, keep the speed
                # constant
                if block_vel > -3 and box.y <=590:
                    block_vel -= .1
                    player_vel += .1
            return score


def controls(keys):
    """"
    this funciton controls the input
    :param keys: keys that we need to call for the controls to work
    :return: nothing used later in the game loop
    """
    if pygame.K_LEFT in keys and box.x >= 15:
        box.x -= player_vel

    if pygame.K_RIGHT in keys and box.x <= 485:
        box.x += player_vel

def game_over(keys):
    """
    function that displays the game over screen
    :param keys: a variable we need for input
    :return: nothing
    """

    # stop the floors from moving
    for floor in floor_left:
        floor.speedy = 0
    for floor in floor_right:
        floor.speedy = 0

    # stop the box from moving
    box.speedy = 0

    # clear everything and display the game over text
    camera.clear('black')
    camera.draw(('Game Over! Score ' + str(score)), 50, 'red', 250, 200)
    camera.draw('Press R to restart', 50, 'red', 250, 260)
    camera.display()

    # checking to see if they reset the game
    if pygame.K_r in keys:

        # call the reset function
        reset()

def reset():
    """
    function that resets the game
    :return: nothing
    """
    global floor_right
    global floor_left
    global block_vel
    global player_vel

    # resetting all of the variables to their original settings

    box.move(250,50)
    floor_right = []
    floor_left = []
    block_vel = -1
    player_vel = 5

    # generating another set of floors
    generate_floors(10)

    # calling teh display function once we have reset everything
    display()

def game(keys):
    """
    the main game loop
    :param keys: the variable we use for the keys to work
    :return: nothing
    """
    global player_vel
    global score

    # calling the score checking function
    get_score()

    # changing the player velocity to the correct velocity once the box is not touching
    if box.speedy != -1:
        box.speedy = player_vel

    # checking to see if it hits the bottom
    if box.y <= 590:
        box.speedy = 0

    # calling the controls function
    controls(keys)


    # check if it the floor
    for floor in floor_left:
        if box.bottom_touches(floor):
            box.move_to_stop_overlapping(floor)

            # if it hits the floor make the box speed = to the floor speed
            box.speedy = floor.speedy
        else:
            box.speedy = player_vel
    for floor in floor_right:
        if box.touches(floor):
            box.move_to_stop_overlapping(floor)
            box.speedy = floor.speedy
        else:
            box.speedy = player_vel
    # get the floors moving
    for floor in floor_left:
        floor.move_speed()

    for floor in floor_right:
        floor.move_speed()

    # run the display function if the box is under the top of the screen
    if box.y >= 0:
        display()

    # if not the game is over
    else:
        game_over(keys)

gamebox.timer_loop(60, game)



