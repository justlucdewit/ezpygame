from ezpg import *#import the module

def setup():#this function runs once
	createCanvas(700, 700)#create 700x700 canvas
	rename("demo1")#set name of the canvas
	background(0, 250, 0)#set background to painfully green

	fill(20, 100, 250)#set fill color to []
	stroke(250, 0, 0)#set stroke color to blue
	strokeWeight(5)#stroke width = 5px
	rect(10, 10, 100, 100)#draw rectangle

	noStroke()#dont use stroke
	fill(250, 0, 0)#fill with blue color
	ellipse(200, 200, 100, 50)#draw a ellipse




def draw():#this function runs 
	pass

#start the application and give the setup and draw functions
start(setup, draw)