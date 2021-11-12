import gamebox
import pygame
import time
import random

# setup and creating some variables that will be used
camera = gamebox.Camera(800,600)
score = 0
lives = 3
blocks = {}
block_size = {}
block_speed = {}
blocks_location = {0:0}
i = 0
start = False

def new_bullet(x,y):

    return gamebox.from_color(x,y,'black',20,10)

def random_block(num):

    for i in range(num):
        blockSize = random.randint(20,50)
        location = []
        x = random.randint(500, 750) + 200
        location.append(x)
        y = random.randint(10, 550)
        location.append(y)
        blocks[i] = (gamebox.from_color(x,y,'blue',blockSize,blockSize))
        blocks_location[i] = location
        block_size[i] = blockSize
        block_speed[i] = -(random.uniform(1.0,2.0))
    return blocks

# create the blocks
random_block(5)

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
base = gamebox.from_color(100,300,'green',5,600)



def tick(keys):
    global bullet
    global score
    global lives
    global i
    global start

    # call shoot function if space is pressed
    if bullet.speedx == 0 and pygame.K_SPACE in keys:
        shoot()

    # next 2 if statements control the shooter

    if pygame.K_UP in keys and shooter.y >= 25:
        shooter.y -=10

    if pygame.K_DOWN in keys and shooter.y <= 600-25:
        shooter.y +=10



    for i in list(blocks):
        if bullet.touches(blocks[i]):
            # changes we make
            bullet.color = 'black'
            del blocks_location[i]
            del blocks[i]
            bullet.speedx = 0
            score += 1
            print(len(blocks))

    # new blocks
    if len(blocks) < 1:
        random_block(10)
        lives +=1

    # next 2 if statements bounce the shooter on the y axis


    if bullet.x >= 800:

        bullet.x = shooter.x
        bullet.color = 'black'
        bullet.speedx = 0
        lives -= 1

    for i in list(blocks):
        if lives < 1 or base.right_touches(blocks[i]):

            camera.clear('black')
            camera.draw("Game Over! Score: "+str(score)+" Press R to restart",50,'red',400,300)
            camera.display()
            return gamebox.pause()
        if pygame.K_r in keys:
            lives = 3
            score = 0
            random_block(10)
    # setting speeds of objects
    for block in blocks:
        blocks[block].move_speed()
    bullet.move_speed()
    shooter.move_speed()

    camera.clear('black')

    # drawing the objects
    camera.draw(base)
    camera.draw(bullet)
    camera.draw(shooter)
    for block in blocks:
        camera.draw(blocks[block])

    # drawing the score and lives
    for i in list(blocks):

        if lives > 0 and base.right_touches(blocks[i]) is False:
            for block in blocks:
                blocks[block].speedx = block_speed[block]

            camera.draw(('Lives: '+str(lives)), 30,"White", 650,10)
            camera.draw(('Score: '+str(score)), 30,"white",740,10)
            camera.display()


gamebox.timer_loop(60, tick)
if pygame.K_r:
    gamebox.unpause()
