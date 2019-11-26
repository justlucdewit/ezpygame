from ezpg import *

b1 = Button(20, 20, 80, 40)
b1.setCaption("Click me!")
b1.setColor(0, 255, 0, 255, 0, 0)

def setup():
	createCanvas(600, 600)
	background(100, 255, 100)

def draw():
	b1.draw()

start(setup, draw)