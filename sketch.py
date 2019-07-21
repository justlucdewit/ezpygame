from ezpg import *

class app(sketch):
	def setup():
		createCanvas(600, 600)
		rename("input test")
		print(isPressed("A"))

	def draw():
		if (isPressed("A")):
			background(255, 0, 0)
		else:
			background(0, 255, 0)

start(app)