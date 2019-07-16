import pygame
pygame.init()

canvas = None

def start(setup, draw):
	setup()
	while True:
		draw()
		update()

def createCanvas(width, height):
	global canvas
	canvas = pygame.display.set_mode((width, height))

def update():
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()