from ezpg import *
#DVD player

x = 0#x pos of the dvd logo
y = 0#y pos of the dvd logo
dx = 0#x velocity of dvd logo
dy = 0#y velocity of dvd logo
dvdwidth = 100#width of dvd
dvdheight = 50#height of dvd
speed = 1#speed of dvd in px/frame

def setup():
	global x
	global y
	global dx
	global dy

	createCanvas(1000, 750)
	

	x = random(0, width()-dvdwidth)#set random x starting coord
	y = random(0, height()-dvdheight)#set random y starting coord

	if random(0, 100)<50:#set random x velocity
		dx = -speed
	else:
		dx = speed

	if random(0, 100)<50:#set random y velocity
		dy = -speed
	else:
		dy = speed

def draw():
	global x
	global y
	global dx
	global dy

	background(0, 0, 0)#fill background to reset the screen

	fill(0, 255, 255)#set dvd color
	rect(x, y, 100, 50)#draw the dvd logo

	x = x+dx#update x pos
	y = y+dy#update y pos

	if x < 0:
		dx = speed

	if y < 0:
		dy = speed

	if x+dvdwidth > width():
		dx = -speed

	if y+dvdheight > height():
		dy = -speed
start(setup, draw)