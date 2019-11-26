from ezpg import *

width = 1000
height = 700



class Ball:
    def __init__(self, dir=69):
        self.radius = 25
        self.x = width/2-self.radius/2
        self.y = height/2+self.radius/2
        self.vy = 0
        self.startSpeed = 0.2
        self.vyrange = 0.5

        if dir == 69:
            r = random(0, 10000)
            if r < 5000:
                self.vx = -self.startSpeed
            else:
                self.vx = self.startSpeed
        
        elif dir == 1:
            self.vx = self.startSpeed
        else:
            self.vx = -self.startSpeed
        
        

    def show(self):
        rect(self.x, self.y, self.radius, self.radius)

    def update(self, p1, p2):
        self.x += self.vx
        self.y += self.vy
        #print(f"x vel = {self.vx}, y vel = {self.vy}")

        #vertical collision
        if self.y < 0 or self.y+self.radius > height:
            self.vy *= -1

        #horizontal collision
        if self.x+self.radius < 0:
            self.__init__(1)
            p2.score += 1
        elif self.x > width:
            self.__init__(-1)
            p1.score += 1

        #padel collision
        if self.x <= p1.x+p1.width and  self.x >= p1.x and self.y+self.radius >= p1.y and self.y <= p1.y + p1.height:
            self.vx *= -1
            val = (self.y+self.radius)-(p1.y)
            newspeed = mapping(val, 0, p1.height+self.radius, -self.vyrange, self.vyrange)
            self.vy = newspeed
        if self.x+self.radius>=p2.x and self.x+self.radius<= p2.x+p2.width and self.y <= p2.y +p2.height and self.y+self.radius >= p2.y:
            self.vx *= -1
            val = (self.y+self.radius)-(p2.y)
            newspeed = mapping(val, 0, p2.height+self.radius, -self.vyrange, self.vyrange)
            self.vy = newspeed


class Padel:
    def __init__(self, x):
        self.x = x
        self.speed = 0.3
        self.width = 20
        self.height = 150
        self.y = height/2-self.height/2
        self.score = 0

    def show(self):
        rect(self.x, self.y, self.width, self.height)

    def input(self, upkey, downkey):
        if isPressed(upkey):
            self.up()
        if isPressed(downkey):
            self.down()

        self.y = constrain(self.y, 0, height-self.height)
    
    def up(self):
        self.y -= self.speed
    
    def down(self):
        self.y += self.speed
        
p1 = Padel(20)
p2 = Padel(960)
ball = Ball()

def displayScore(num1, num2):
    fill(200, 200, 200)
    text(str(num1), width/2-80, 80)
    text(str(num2), width/2+80, 80)

def drawMiddleLine():
    for i in range(7):
        rect(width/2-5, i*100+25, 10, 50)

def setup():
    createCanvas(width, height)
    noStroke()
   
def draw():
    background(0, 0, 0)
    p1.show()
    p2.show()
    p1.input("W", "S")
    p2.input("up", "down")

    ball.show()
    ball.update(p1, p2)
    displayScore(p1.score, p2.score)
    drawMiddleLine()

start(setup, draw)