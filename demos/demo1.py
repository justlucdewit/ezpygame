from ezpg import *#import the module

def setup():#this function runs once
	createCanvas(700, 700)#create 700x700 canvas
	rename("demo1")#set name of the canvas
	background(0, 255, 0)#set background to painfully green

def draw():#this function runs 
	pass

#start the application and give the setup and draw functions
start(setup, draw)