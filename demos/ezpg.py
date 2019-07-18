import pygame
import sys
import random as r

canvas = None
fillcolor = (255, 255, 255, 255)
strokecolor = (0, 0, 0, 255)
w = 0
h = 0
sw = 1

def start(setup, draw):
	setup()
	while True:
		draw()
		__update__()

def createCanvas(width, height):
	global canvas
	global w
	global h
	
	w = width
	h = height

	print(w)

	canvas = pygame.display.set_mode((width, height))
	pygame.display.set_caption("sketch")

def __update__():
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

def mouseX():
	return pygame.mouse.get_pos()[0]

def mouseY():
	return pygame.mouse.get_pos()[1]

def rename(name):
	pygame.display.set_caption(name)

def background(r, g, b):
	canvas.fill((r,g,b))

def rect(x, y, width, height):
	pygame.draw.rect(canvas, fillcolor, (x, y, width, height), 0)
	if strokecolor[3] != 0:
		pygame.draw.rect(canvas, strokecolor, (x, y, width, height), sw)

def fill(r,g,b,a=255):
	global fillcolor
	fillcolor = (r,g,b,a)

def stroke(r,g,b,a=255):
	global strokecolor
	strokecolor = (r,g,b,a)

def noStroke():
	global strokecolor
	strokecolor = (0,0,0,0)

def noFill():
	global fillcolor
	fillcolor = (0,0,0,0)

def strokeWeight(weight):
	global sw
	sw = weight

def ellipse(x, y, width, height):
	pygame.draw.ellipse(canvas, fillcolor, (x, y, width, height), 0)
	if strokecolor[3] != 0:
		pygame.draw.ellipse(canvas, strokecolor, (x, y, width, height), sw)

def random(min, max):
	return r.uniform(min, max)

def width():
	return w

def height():
	return h

def mapping(n, imin, imax, omin, omax):
	return omin+(omax-omin)*(n-imin)/(imax-imin)