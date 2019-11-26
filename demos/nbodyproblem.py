from ezpg import *

class body():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20

    def render(self):
        fill(255, 255, 255)
        ellipse(self.x, self.y, self.radius, self.radius)

bodies = []
numOfBodies = 5


def setup():
    createCanvas(600, 600)
    for i in range(numOfBodies):
        bodies.append(body(random(0, width), random(0, height)))

def draw():
    background(0, 0, 0)

start(setup, draw)

