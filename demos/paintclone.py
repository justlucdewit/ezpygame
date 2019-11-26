from ezpg import *

def changecolor():
	c = promptColor()
	if c != None:
		fill(c[0], c[1], c[2])

def clearscreen():
	background(255, 255, 255)

pensize = 20
mode = "pen"
menuwidth = 120

button_newcolor = Button(20, 20, 80, 40)
button_newcolor.onClick = changecolor
button_newcolor.setColor(0, 255, 0, 255, 0, 0)
button_newcolor.caption = "Color"

button_clear = Button(20, 80, 80, 40)
button_clear.onClick = clearscreen
button_clear.setColor(0, 255, 0, 255, 0, 0)
button_clear.caption = "Clear"

penIco = (#sized 24x24
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                XX      ",
  "               X..X     ",
  "              XX...X    ",
  "             X..X X     ",
  "            X....X      ",
  "           X....X       ",
  "          X....X        ",
  "         X....X         ",
  "        X....X          ",
  "       X....X           ",
  "      X....X            ",
  "     XX...X             ",
  "    X..X.X              ",
  "    X...X               ",
  "    XXXX                ",
  "                        ",
  "                        ",
  "                        ",
  "                        ")

sprayIco = (#sized 24 24
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "   X                    ",
  "                        ",
  "        X               ",
  "              XXXXXXXX  ",
  "   X    X    XX......X  ",
  "              X......X  ",
  "       X    XXXXXXXXXXXX",
  "            X..........X",
  "   X        X..........X",
  "            X..........X",
  "            X..........X",
  "            X..........X",
  "            X..........X",
  "            X..........X",
  "            X..........X",
  "            X..........X",
  "            X..........X",
  "            X..........X",
  "            X..........X",
  "            XXXXXXXXXXXX")

def createCursor(curs):
	cursor, mask = pygame.cursors.compile(curs, "X", ".")
	cursor_sizer = ((24, 24), (12, 12), cursor, mask)
	pygame.mouse.set_cursor(*cursor_sizer)

def setup():
	createCanvas(600+menuwidth, 600)
	rename("luke paint")
	fill(0, 0, 0)
	noStroke()
	background(255, 255, 255)
	createCursor(penIco)

def draw():
	global mode
	global pensize
	rect(0, 0, menuwidth, height())
	pensize = constrain((scroll()*-1)+pensize, 5, 80)

	if isPressed("lmb") and mouseX() > menuwidth:
		if mode == "pen":
			toolPen()

		if mode == "spray":
			toolSpray()

	if isPressed("P"):
		mode = "pen"
		createCursor(penIco)

	if isPressed("S"):
		mode = "spray"
		createCursor(sprayIco)

	button_newcolor.draw()
	button_clear.draw()

def toolPen():
	ellipse(mouseX()-pensize/2, mouseY()-pensize/2, pensize, pensize)

def toolSpray():
	ellipse(mouseX()+random(-pensize/2, pensize/2), mouseY()+random(-pensize/2, pensize/2), 1,1)

start(setup, draw)