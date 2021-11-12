import pygame
import random
import gamebox


score = 0
width = 500
height = 600
r_x = width/2
camera = gamebox.Camera(width, height)
floor_left = {}
floor_right = {}


box = gamebox.from_color(50,50,'red',20,20)
num_floors = 100
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
        floor_left[i] = gamebox.from_color(((600-right_size-40)/2),floor_location,'white',left_size,20)
        floor_right[i] = gamebox.from_color(((600+left_size+40)/2),floor_location,'white',right_size,20)
        floor_location -= 50

generate_floors(num_floors)

for floors in floor_left:
    floor_left[floors].speedy = -1

for floors in floor_right:
    floor_right[floors].speedy = -1

box.speedy = 5
def display():
    box.move_speed()
    camera.clear('black')
    for floors in floor_left:
        camera.draw(floor_left[floors])
    for floors in floor_right:
        camera.draw(floor_right[floors])
    camera.draw(box)
    camera.draw(('Score: ' + str(score)), 30, "red", 440, 10)
    camera.display()

def tick(keys):
    global score
    # next 2 statements check to see if the box has touched a floor
    box.speedy = 5

    # trying to check to see if there is a score
    for i in list(floor_left):
        if box.bottom_touches(floor_left[i]):
            box.speedy = floor_left[i].speedy

    for i in list(floor_left):
        print(box.y - floor_left[i].y)
        print(box.speedy)
        if floor_left[i].y - box.y <= 10 >=0 and box.speedy == floor_left[i].speedy:
            score += 1

    # left right controller
    if pygame.K_LEFT in keys and box.x >= 15:
        box.x += -10

    if pygame.K_RIGHT in keys and box.x <= 480:
        box.x += 10

    # checking to see if it hits the bottom
    if box.y >= 590:
        box.speedy = 0

    # check if it the floor
    for i in list(floor_left):
        box.move_to_stop_overlapping(floor_left[i])
    for i in list(floor_right):
        box.move_to_stop_overlapping(floor_right[i])

    # check if left box hits left side
    for floors in floor_left:
        floor_left[floors].move_speed()

    for floors in floor_right:
        floor_right[floors].move_speed()

    if box.y >= 0:
        display()

    else:
        for floors in floor_left:
            floor_left[floors].speedy = 0

        for floors in floor_right:
            floor_right[floors].speedy = 0
        box.speedy = 0
        camera.clear('black')
        camera.draw(('Game Over! Score ' + str(score)), 50, 'red', 250, 200)
        camera.draw('Press R to restart', 50, 'red', 250, 260)
        camera.display()

        if pygame.K_r in keys:
            pass

gamebox.timer_loop(30, tick)
# this line of code will not be reached until after the window is closed

