from ezpg import *

penSize = 10

def setup():
    createCanvas(600, 600)
    background(255, 255, 255)
    fill(255, 255, 255)

def draw():
    if isPressed("lmb"):
        ellipse(mouseX()-penSize/2, mouseY()-penSize/2, penSize, penSize)

start(setup, draw)
