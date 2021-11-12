import pygame
import random
import gamebox


score = 0
width = 500
height = 600
r_x = width/2
camera = gamebox.Camera(width, height)
floor_left = []
floor_right = []
hitbox = []
player_vel = 5
box = gamebox.from_color(50,50,'red',20,20)
num_floors = 10
floor_location = (num_floors*50)+200

def generate_floors(num):
    '''
    whant to generate 2 blocks with a gap of 40 between each other
    :return: nothing using global dictionaries
    '''
    global floor_location

    for i in range(num):
        left_size = random.randint(0, 280)
        right_size = (600 - left_size - 40)
        floor_left.append(gamebox.from_color(((600-right_size-40)/2),floor_location,'white',left_size,20))
        floor_right.append(gamebox.from_color(((600+left_size+40)/2),floor_location,'white',right_size,20))
        floor_location -= 50


generate_floors(num_floors)

for floor in floor_left:
    floor.speedy = -1

for floor in floor_right:
    floor.speedy = -1

for hitboxes in hitbox:
    hitboxes.speedy = -1

def display():
    camera.clear('black')
    for floor in floor_left:
        camera.draw(floor)
    for floor in floor_right:
        camera.draw(floor)

    camera.draw(box)
    camera.draw(('Score: ' + str(score)), 30, "red", 440, 10)
    camera.display()
    if box.speedx == 0:
        box.speedy = 5
        box.move_speed()

def get_score():
    global score
    for floor in floor_left:
        if box.y >= floor.y:
            score = len(floor_left) - floor_left.index(floor)
            return score

def controls(keys):
    if pygame.K_LEFT in keys and box.x >= 15:
        box.x -= 5

    if pygame.K_RIGHT in keys and box.x <= 485:
        box.x +=5

    # checking to see if it hits the bottom
    if box.y >= 590:
        box.speedy = 0

def tick(keys):
    global score

    get_score()

    if box.speedy != -1:
        box.speedy = 5
    # next 2 statements check to see if the box has touched a floor

    controls(keys)
    # check if it the floor
    for floor in floor_left:
        if box.touches(floor):
            box.move_to_stop_overlapping(floor)
            box.speedy = floor.speedy
    for floor in floor_right:
        if box.touches(floor):
            box.move_to_stop_overlapping(floor)
            box.speedy = floor.speedy

    # get the floors moving
    for floor in floor_left:
        floor.move_speed()

    for floor in floor_right:
        floor.move_speed()

    for hitboxes in hitbox:
        hitboxes.move_speed()

    if box.y >= 0:
        display()

    else:
        for floor in floor_left:
            floor.speedy = 0

        for floor in floor_right:
            floor.speedy = 0
        box.speedy = 0
        camera.clear('black')
        camera.draw(('Game Over! Score ' + str(score)), 50, 'red', 250, 200)
        camera.draw('Press R to restart', 50, 'red', 250, 260)
        camera.display()

        if pygame.K_r in keys:
            pass

gamebox.timer_loop(60, tick)
# this line of code will not be reached until after the window is closed

