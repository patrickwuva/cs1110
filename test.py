# Shooting hoops example code

import pygame
import gamebox

camera = gamebox.Camera(800, 600)

# scenery
court = gamebox.from_color(400, 550, 'blue', 600, 50)
backboard = gamebox.from_color(650, 280, 'white', 10, 150)
hoop = gamebox.from_image(610, 350, 'hoop.png')
# https://www.vhv.rs/viewpic/hTmTJoR_transparent-basketball-hoop-silhouette-hd-png-download/
hoop.scale_by(0.5)
scenery = [court, backboard, hoop]  # Things that are stationary
obstacles = [court, backboard]  # things that are "solid"

# interactive
ball = gamebox.from_circle(200, 50, 'orangered', 20)

# stats
score = 0
lives = 3

# physics
gravity = 0.9
jump_speed = 25

# other
scored_since_landed = False

def draw_scenery():
	#Draw all the stationary items
	for item in scenery:
		camera.draw(item)

def draw_stats():
	#draws the gameplay information (lives, score)
	score_text = "Score: " + str(score)
	camera.draw(score_text, 36, 'red', 50, 20)
	for i in range(lives):
		heart = gamebox.from_image(775, 25, 'heart3.png')
		#https://www.pngegg.com/en/png-wwcar
		heart.x -= 50 * i
		heart.scale_by(0.5)
		camera.draw(heart)

def move_ball(keys):
	#Determines where the ball should be by checking for user input and obstacles
	global scored_since_landed
	if pygame.K_RIGHT in keys:
		ball.speedx += 1
	if pygame.K_LEFT in keys:
		ball.speedx -= 1
	for obstacle in obstacles:
		if ball.bottom_touches(obstacle):
			scored_since_landed = False
			if pygame.K_UP in keys:
				ball.speedy = -jump_speed
	ball.speedy += gravity
	ball.move_speed()
	for obstacle in obstacles:
		ball.move_to_stop_overlapping(obstacle)

def points_scored():
	#Checks if the user scored a basket this tick
	global scored_since_landed
	if ball.touches(hoop) and not scored_since_landed and ball.speedy > 0:
		scored_since_landed = True
		return 2
	return 0

def out_of_bounds():
	global score
	# if you hit the rim from the underside
	if ball.touches(hoop) and ball.speedy < 0:
		ball.speedy *= -1
		return False
	#checks if the ball is out of bounds
	return ball.y > 600

def reset_ball():
	#replace the ball when it's out of bounds
	ball.x = 200
	ball.y = 50
	ball.speedx = 0
	ball.speedy = 0

def game_over():
	#checks if there is a game over, draws things based on that
	if lives == 0:
		camera.draw(gamebox.from_text(400, 300, 'You Lose', 42, 'white', True))
		camera.display()
		return True
	return False

def tick(keys):
	global score, lives
	camera.clear('black')
	if game_over():
		return
	draw_scenery()
	draw_stats()
	move_ball(keys)
	score += points_scored()
	if out_of_bounds():
		lives -= 1
		reset_ball()
	camera.draw(ball)
	camera.display()

gamebox.timer_loop(30, tick)