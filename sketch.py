from ezpg import *

def setup():
	createCanvas(700, 700)
	rename("game")
	background(255, 0, 255)
	rect(50, 50, 200, 200)

def draw():
	pass

start(setup, draw)