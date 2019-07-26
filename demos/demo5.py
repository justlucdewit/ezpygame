from ezpg import *

#graph calculator

ww = 600#window width
wh = 600#window height

minX = -10
maxX = 10
minY = -10
maxY = 10

bg = (255, 255, 255)#background color
mainAxisColor = (0, 0, 0)#main axis color
gridColor = (200, 200, 200)
def setup():
	createCanvas(ww, wh)
	transform(width()/2, height()/2)
	background(*bg)
		

	#create the main axis
	strokeWeight(2)
	fill(*mainAxisColor)
	line(-width()/2, 0, width()/2, 0)
	line(0, -height()/2, 0, height()/2)

	#create grid

def draw():
	pass

start(setup, draw)
