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
        self.y = constrain(self.y, 0, height()-self.height)

#ball class
class Ball():
    def __init__(self):#initiation function
        self.minspeed = 0.2
        self.maxspeed = 1
        self.x = width()/2
        self.y = height()/2
        self.r = 10
        self.vx = 0
        self.vy = 0

        if random(0, 1000) < 500:
            self.vx= random(self.minspeed, self.maxspeed)
        else:
            self.vx = random(-self.maxspeed, -self.minspeed)

        if random(0, 1000) < 500:
            self.vy = random(self.minspeed, self.maxspeed)
        else:
            self.vy = random(-self.maxspeed, -self.minspeed)

    def draw(self):#draw function
        rect(self.x, self.y, 2*self.r, 2*self.r)
    
    def move(self):
        self.x += self.vx
        self.y += self.vy
        
        #vertical bouncing
        if self.y+self.r > height():
            self.vy *= -1
        elif self.y-self.r < 0:
            self.vy *= -1

#main sketch class
class ponggame(sketch):
    p1 = None#paddle object
    p2 = None#paddle object
    b = None#ball object

    def setup(self):
        global p1#this is needed so you
        global p2#are able to set this to a value
        global b

        createCanvas(800, 600)#create the canvas
        rename("pong")
        p1 = paddle(10, height()/2)#create p1 object
        p2 = paddle(width()-30, height()/2)#create p2 object
        b = Ball()

    def draw(self):
        background(0, 0, 0)#set background
        p1.draw()#draw player 1's paddle
        p2.draw()#draw player 2's paddle
        b.draw()#draw the ball
        b.move()#move the ball

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
