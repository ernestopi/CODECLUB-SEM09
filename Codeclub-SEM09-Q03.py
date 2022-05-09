# formatos em loop
from turtle import *
shape('turtle')
speed(8)

# pentágono
for count in range(5):
    forward(100)
    right(72)

penup()
forward(250)
pendown()

# hexágono
for count in range(6):
    forward(100)
    right(60)

penup()
forward(250)
pendown()

# círculo
for count in range(360):
    forward(1)
    right(1)

done()