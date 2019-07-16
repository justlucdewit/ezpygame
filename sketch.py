from ezpg import *

def setup():
	createCanvas(700, 700)
	rename("game")
	background(255, 0, 255)

	fill(255, 0, 0)
	strokeWeight(5)
	stroke(50, 50, 255)
	rect(50, 50, 200, 200)

	fill(0, 255, 0)
	noStroke()
	rect(100, 100, 100, 100)


def draw():
	pass

start(setup, draw)