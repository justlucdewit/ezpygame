import pygame
import sys
import random as r

canvas = None
fillcolor = (255, 255, 255, 255)
strokecolor = (0, 0, 0, 255)
w = 0
h = 0
sw = 1
tcol = [0, 0, 0]

keycodes = {
	"A": 97,
	"B": 98,
	"C": 99,
	"D": 100,
	"E": 101,
	"F": 102,
	"G": 103,
	"H": 104,
	"I": 105,
	"J": 106,
	"K": 107,
	"L": 108,
	"M": 109,
	"N": 110,
	"O": 111,
	"P": 112,
	"Q": 113,
	"R": 114,
	"S": 115,
	"T": 116,
	"U": 117,
	"V": 118,
	"W": 119,
	"X": 120,
	"Y": 121,
	"Z": 122,
	"0": 48,
	"1": 49,
	"2": 50,
	"3": 51,
	"4": 52,
	"5": 53,
	"6": 54,
	"7": 55,
	"8": 56,
	"9": 57,
	"left": 276,
	"right": 275,
	"up": 273,
	"down": 274,
}

class sketch():
	def setup():
		pass

	def draw():
		pass


pygame.init()
font = pygame.font.SysFont('Arial', 30)

def start(app):
	app.setup()
	while True:
		app.draw()
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

def text(txt, x, y):
	t = font.render(txt, False, (tcol[0], tcol[1], tcol[2]))
	canvas.blit(t,(x,y))

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

def isPressed(key):
	if pygame.key.get_pressed()[keycodes[key]] == 1:
		return True
	else:
		return False