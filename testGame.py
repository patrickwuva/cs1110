import gamebox
import pygame
import time
import random

# setup and creating some variables that will be used
camera = gamebox.Camera(800,600)
score = 0
lives = 3
logo = gamebox.from_image(0,0, "https://www.python.org/static/img/python-logo.png")
blocks = {}
block_size = {}
blocks_location = {}
i = 0


def new_bullet(x,y):
    '''
    generates a new bullet
    :param x: x cord of the shooter
    :param y: y cord of the shooter
    :return: returns a new object which is the bullet.
    '''
    return gamebox.from_color(x,y,'black',20,10)

def random_block(num):

    for i in range(num):
        blockSize = random.randint(10,50)
        location = []
        x = random.randint(500, 750)
        location.append(x)
        y = random.randint(0, 550)



        location.append(y)
        blocks[i] = (gamebox.from_color(x,y,'blue',blockSize,blockSize))
        blocks_location[i] = location
        block_size[i] = blockSize
    return blocks

# create the blocks
random_block(10)


def shoot():
    '''
    Function that shoots the bullet
    :return: nothing
    '''
    global bullet
    bullet = new_bullet(shooter.x,shooter.y)
    bullet.color = 'white'
    bullet.speedx = 20

# create the shooter and bullet and get the shooter moving
shooter = gamebox.from_color(50,100,'red',50,50)
shooter.speedy = 0
bullet = new_bullet(5,10)




def tick(keys):
    global bullet
    global score
    global lives
    global i

    # call shoot function if space is pressed
    if bullet.speedy == 0 and pygame.K_SPACE in keys:
        shoot()
    # next 4 if statements control the shooter
    if pygame.K_LEFT in keys and shooter.x >= 15:
        shooter.x -=10

    if pygame.K_RIGHT in keys and shooter.x <= 785:
        shooter.x += 10

    if pygame.K_UP in keys and shooter.y >= 25:
        shooter.y -=10

    if pygame.K_DOWN in keys and shooter.y <= 600-25:
        shooter.y +=10

    # check to see if bullet is within proximity of a square
    for i in list(blocks_location):
        if (blocks_location[i][0] - bullet.x) <= ((block_size[i]/2)+5) and (blocks_location[i][0] - bullet.x) >=-((block_size[i]/2)-5) and ((block_size[i]/2)+5)>= (
                blocks_location[i][1] - bullet.y) >= -((block_size[i]/2)-5):

            # for debugging
            print('bullet location: ',bullet.x,bullet.y,"blocks location: ",blocks_location[i][0],blocks_location[i][1])
            print('x difference: ',blocks_location[i][0]-bullet.x)
            print('y difference: ',blocks_location[i][1]-bullet.y)


            # changes we make
            bullet.color = 'black'
            del blocks_location[i]
            del blocks[i]
            bullet.speedx = 0
            score += 1


    # next 2 if statements bounce the shooter on the y axis

    if shooter.y >= 575:
        shooter.speedy = -20

    if shooter.y <= 15:
        shooter.speedy = 20

    if bullet.x >= 800:

        bullet.x = shooter.x
        bullet.color = 'black'
        bullet.speedx = 0
        lives -= 1
    # ***Needs work*** trying to kill the game and restart when the shooter runs out of lives
    if lives == 0:
        False
    # setting speeds of objects
    bullet.move_speed()
    shooter.move_speed()

    camera.clear('black')

    # drawing the objects
    camera.draw(bullet)
    camera.draw(shooter)
    for block in blocks:
        camera.draw(blocks[block])

    # drawing the score and lives
    camera.draw(('Lives: '+str(lives)), 30,"White", 650,10)
    camera.draw(('Score: '+str(score)), 30,"white",740,10)
    camera.display()



gamebox.timer_loop(60, tick)

