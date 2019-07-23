from ezpg import *

#paddle class
class paddle():
    def __init__(self, x, y):#initiation function
        self.height = 200
        self.width = 20
        self.x = x
        self.y = y-self.height

    def draw(self):#for displaying stuff to the screen
        rect(self.x, self.y, self.width, self.height)
    
    def move(self, speed):#for moving the paddles
        self.y += speed

#main sketch class
class ponggame(sketch):
    p1 = None#paddle object
    p2 = None#paddle object
    
    def setup(self):
        global p1#this is needed so you
        global p2#are able to set this to a value

        createCanvas(800, 600)#create the canvas
        rename("pong")
        p1 = paddle(10, height()/2)#create p1 object
        p2 = paddle(width()-30, height()/2)#create p2 object

    def draw(self):
        background(0, 0, 0)#set background
        p1.draw()#draw player 1's paddle
        p2.draw()#draw player 2's paddle

        #handle movement
        if isPressed("Q"):
            p1.move(-1)
        if isPressed("A"):
            p1.move(1)
        if isPressed("up"):
            p2.move(-1)
        if isPressed("down"):
            p2.move(1)

start(ponggame())
