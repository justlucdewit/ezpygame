# ezpg
#### easy-pygame
##### hey there!, thanks for looking into ezpg
##### ezpg is a python module used for creating quick
##### and easy python games/visualizations

##### its based on the famous processing framework wich
##### is verry beginners friendly yet verry powerfull



#### functions: 

##### start(setup, draw)
```
starts the application

setup)	[func] a function wich gets called on start
draw)	[func] a function wich get called once per frame
```

##### createCanvas(width, height)
```
creates window object

height) [int] height of the canvas in pixels
width)	[int] width of canvas in pixels
```

##### rename(name)


```
renames the window object

name)	[str] the name of the window object
```

##### background(r, g, b)
```
changes the background color

r)	[int] r color value of the background color from 0 to 255
g)	[int] g color value of the background color from 0 to 255
b)	[int] b color value of the background color from 0 to 255
```


#####fill(r, g, b)
```
changes fill colors of all shapes drawn after this

r)	[int] r color value of the fill color from 0 to 255
g)	[int] g color value of the fill color from 0 to 255
b)	[int] b color value of the fill color from 0 to 255
```

#####noFill()
```
makes sure that all shapes drawn after this are transparent except the stroke

*no arguments*
```

#####stroke(r, g, b)
```
sets color of the edge of the shape (the stroke)

r)	[int] r color value of the stroke color from 0 to 255
g)	[int] g color value of the stroke color from 0 to 255
b)	[int] b color value of the stroke color from 0 to 255
```

#####noStroke()
```
makes sure that all shapes drawn after this have a transparent stroke

*no arguments*
```
#####strokeWeight(weight)
```
sets the thinkness of the stroke of all shapes drawn after this

weight) [int] the width of the stroke in pixels
```

#####rect(x, y, width, height)
```
draws a rectangle on the screen

x)		[int/float] x coordinate of left upper corner
y)		[int/float] y coordinate of left upper corner
width)	[int/float] width of the rectangle
height)	[int/float] height of the rectangle
```
