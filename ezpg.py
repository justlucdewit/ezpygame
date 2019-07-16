import pygame
pygame.init()

canvas = None
fillcolor = (0, 0, 0)

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
	pygame.draw.rect(canvas, fillcolor, (x, y, width, height))

def ellipse(x, y, width, height):
	pass
