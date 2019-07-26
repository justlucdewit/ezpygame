import pygame
import sys
import random as r
from addons.keycodes import *

canvas = None
fillcolor = (255, 255, 255, 255)
strokecolor = (0, 0, 0, 255)
w = 0
h = 0
sw = 1
tcol = [0, 0, 0]

#translation
xt = 0
yt = 0


class sketch():
	def setup():
		pass

	def draw():
		pass


pygame.init()
font = pygame.font.SysFont('Arial', 30)

def start(s, d):
	s()
	while True:
		d()
		__update__()

def createCanvas(width, height):
	global canvas
	global w
	global h
	
	w = width
	h = height

	canvas = pygame.display.set_mode((width, height))
	pygame.display.set_caption("sketch")

def __update__():
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

def text(txt, x, y):
	t = font.render(txt, False, (tcol[0], tcol[1], tcol[2]))
	canvas.blit(t,(x+xt,y+yt))

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
	global tcol
	tcol = [r, g, b]
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
	pygame.draw.ellipse(canvas, fillcolor, (x+xt, y+yt, width, height), 0)
	if strokecolor[3] != 0:
		pygame.draw.ellipse(canvas, strokecolor, (x+xt, y+yt, width, height), sw)

def random(min, max):
	return r.uniform(min, max)

def width():
	return w

def height():
	return h

def mapping(n, imin, imax, omin, omax):
	return omin+(omax-omin)*(n-imin)/(imax-imin)

def isPressed(key):
	if pygame.key.get_pressed()[keycodes[key]] == 1:
		return True
	else:
		return False

def constrain(n, min, max):
	if n < min:
		return min
	if n > max:
		return max
	else:
		return n

def line(x1, y1, x2, y2):
	pygame.draw.line(canvas, fillcolor, (x1+xt, y1+yt), (x2+xt, y2+yt), sw)
	
def transform(x, y):
	global xt
	global yt
	xt = x
	yt = y 