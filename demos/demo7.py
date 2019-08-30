from ezpg import *
from math import *

cols = None
rows = None
grid = []
stack = []
w = 10
wi = 600
he = 700

if w < 5:
	print("cells cant be smaller then 5")
	exit()
if wi < 50:
	print("screen width cant be less then 50")
	exit()
if wi > 1400:
	print("screen width cant be more then 1400")
	exit()
if he < 50:
	print("screen height cant be less then 50")
	exit()
if he > 800:
	print("screen height cant be more then 800")
	exit()

def getIndex(i, j):
	if i < 0 or j < 0 or i > rows-1 or j > cols-1:return None;
	return j+i*cols

def removeWalls(c, n):
	if c != None and n != None:
		x = c.i - n.i
		if x == 1:
			c.walls[3] = False
			n.walls[1] = False
		elif x == -1:
			c.walls[1] = False
			n.walls[3] = False
		y = c.j - n.j
		if y == 1:
			c.walls[0] = False
			n.walls[2] = False
		elif y == -1:
			c.walls[2] = False
			n.walls[0] = False

class Cell():
	def __init__(self, i, j):
		self.i = i
		self.j = j
		self.walls = [True, True, True, True]
		self.visited = False

	def show(self, forced=False):
		x = self.i*w
		y = self.j*w

		if not forced:
			if self.visited:
				noStroke()
				fill(255, 0, 255, 100)
				rect(x, y, w, w)

			fill(255, 255, 255)

			if self.walls[0]:
				line(x,y,x+w,y)

			if self.walls[1]:
				line(x+w,y+w,x+w,y)

			if self.walls[2]:
				line(x,y+w,x+w,y+w)

			if self.walls[3]:
				line(x,y,x,y+w)
		else:
			fill(0, 0, 0)

			if self.walls[0]:
				line(x,y,x+w,y)

			if self.walls[1]:
				line(x+w,y+w,x+w,y)

			if self.walls[2]:
				line(x,y+w,x+w,y+w)

			if self.walls[3]:
				line(x,y,x,y+w)

		return self.visited

	def highlight(self):
		fill(0, 255, 0, 100)
		rect(self.i*w, self.j*w, w, w)

	def checkNeighbors(self):
		neighbors = []

		ctop = getIndex(self.i, self.j-1)
		if ctop != None:
			top = grid[ctop]
		else:
			top = None

		cbottom = getIndex(self.i, self.j+1)
		if cbottom != None:
			bottom = grid[cbottom]
		else:
			bottom = None

		cleft = getIndex(self.i-1, self.j)
		if cleft != None:
			left = grid[cleft]
		else:
			left = None

		cright = getIndex(self.i+1, self.j)
		if cright != None:
			right = grid[cright]
		else:
			right = None

		if (top != None and not top.visited ):neighbors.append(top)
		if (bottom != None and not bottom.visited):neighbors.append(bottom)
		if (left != None and not left.visited):neighbors.append(left)
		if (right != None and not right.visited):neighbors.append(right)

		if len(neighbors) > 0:
			r = floor(random(0, len(neighbors)))
			return neighbors[r]
		else:
			return None

def setup():
	global cols
	global rows
	global grid
	global current

	createCanvas(wi, he)
	cols = floor(height()/w)
	rows = floor(width()/w)

	for i in range(rows):
		for j in range(cols):
			cell = Cell(i, j)
			grid.append(cell)
	current = grid[0]

def draw():
	global current
	done = False
	while not done:
		background(50, 50, 50)
		done = True
		for cell in grid:
			if not cell.show():
				done = False

		current.visited = True
		current.highlight()

		next = current.checkNeighbors()
			
		if next != None:
			next.visited = True
			stack.append(current)
			removeWalls(current, next)
			current = next
		elif len(stack)>0:
			current = stack.pop(0)
		update()

	background(255, 255, 255)

	grid[0].walls[3] = False
	grid[-1].walls[1] = False

	for cell in grid:
		cell.show(True)

	while True:
		update()

start(setup, draw)