from ezpg import *
#DVD player

x = 0#x pos of the dvd logo
y = 0#y pos of the dvd logo
dx = 0#x velocity of dvd logo
dy = 0#y velocity of dvd logo
dvdwidth = 100#width of dvd
dvdheight = 50#height of dvd
speed = 1#speed of dvd in px/frame
color = [0, 255, 255]

def setup():
	global x
	global y
	global dx
	global dy

	createCanvas(1000, 750)
	rename("WILL IT HIT DA CORNER???")

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
	global color
	hit = False

	background(0, 0, 0)#fill background to reset the screen

	fill(*color)#set dvd color
	rect(x, y, dvdwidth, dvdheight)#draw the dvd logo

	fill(255, 255, 255)#set text color
	text("DVD", x+10, y)#draw text

	x = x+dx#update x pos
	y = y+dy#update y pos

	if x < 0:
		dx = speed
		hit = True

	if y < 0:
		dy = speed
		hit = True

	if x+dvdwidth > width():
		dx = -speed
		hit = True

	if y+dvdheight > height():
		dy = -speed
		hit = True

	#randomize color
	if hit:
		color = [round(random(0, 255)), round(random(0, 255)), round(random(0, 255))]

start(setup, draw)