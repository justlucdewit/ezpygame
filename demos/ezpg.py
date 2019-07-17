import pygame
pygame.init()

canvas = None
fillcolor = (255, 255, 255, 255)
strokecolor = (0, 0, 0, 255)
sw = 1

def start(setup, draw):
	setup()
	while True:
		draw()
		__update__()

def createCanvas(width, height):
	global canvas
	canvas = pygame.display.set_mode((width, height))
	pygame.display.set_caption("sketch")

def __update__():
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

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