import pygame
import sys
import random as r
from addons.keycodes import *

from tkinter.colorchooser import *
import tkinter as tk

canvas = None
fillcolor = (255, 255, 255, 255)
strokecolor = (0, 0, 0, 255)
w = 0
h = 0
sw = 1
tcol = [0, 0, 0]

#translation
xt = 0
yt = 0

fs = 30

def promptColor():
	root = tk.Tk()
	root.withdraw()
	color = askcolor()[0]
	root.destroy()
	return color

class Button():
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.capt = ""
		self.fs = 20
		self.normcol = []
		self.presscol = []

	def draw(self):
		#store variables that need reset
		tmp1 = fs
		tmp2 = fillcolor

		fill(*self.normcol)
		if isPressed("lmb") and mouseX()>self.x and mouseX()<self.x+self.w and mouseY()>self.y and mouseY()<self.y+self.h:
			fill(*self.presscol)

		fontSize(self.fs)
		rect(self.x, self.y, self.w, self.h)
		fill(*tmp2)
		text(self.capt, self.x+5, self.y)

		#reset the variables
		fill(*tmp2)
		fontSize(tmp1)


	def setCaption(self, txt, size=20):
		self.capt = txt
		self.fs = size

	def setColor(self, nr, ng, nb, pr, pg, pb):
		self.normcol = [nr,ng,nb]
		self.presscol = [pr,pg,pb]


class sketch():
	def setup():
		pass

	def draw():
		pass


pygame.init()
font = pygame.font.SysFont('Arial', 30)

def seticon(image):
	pygame.display.set_icon(image)

def start(s, d):
	s()
	while True:
		d()
		update()

def fontSize(size):
	global font
	global fs
	fs = size
	font = pygame.font.SysFont('Arial', size)

def getFontSize():
	return fs

def createCanvas(width, height):
	global canvas
	global w
	global h
	
	w = width
	h = height

	canvas = pygame.display.set_mode((width, height), pygame.SRCALPHA)
	pygame.display.set_caption("sketch")

def update():
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

def text(txt, x, y):
	t = font.render(txt, False, (tcol[0], tcol[1], tcol[2]))
	canvas.blit(t,(x+xt,y+yt))

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
	pygame.draw.ellipse(canvas, fillcolor, (x+xt, y+yt, width, height), 0)
	if strokecolor[3] != 0:
		pygame.draw.ellipse(canvas, strokecolor, (x+xt, y+yt, width, height), sw)

def random(min, max):
	return r.uniform(min, max)

def width():
	return w

def height():
	return h

def mapping(n, imin, imax, omin, omax):
	return omin+(omax-omin)*(n-imin)/(imax-imin)

def isPressed(key):
	if key != "lmb" and key != "rmb" and key != "mmb":
		if pygame.key.get_pressed()[keycodes[key]] == True:
			return True
	else:
		if pygame.mouse.get_pressed()[keycodes[key]] == True:
			return True
	return False

def constrain(n, min, max):
	if n < min:
		return min
	if n > max:
		return max
	else:
		return n

def line(x1, y1, x2, y2):
	pygame.draw.line(canvas, fillcolor, (x1+xt, y1+yt), (x2+xt, y2+yt), sw)
	
def transform(x, y):
	global xt
	global yt
	xt = x
	yt = y 

def image(i, x, y):
	canvas.blit(i,(x+xt,y+yt))

def imageScale(i, w, h):
	return pygame.transform.scale(i, (w, h))

def loadImage(url):
	return pygame.image.load(url)