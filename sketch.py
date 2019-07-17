from ezpg import *

def setup():
	createCanvas(700, 700)
	yell()

def draw():
	rename(str(mouseX()))

start(setup, draw)