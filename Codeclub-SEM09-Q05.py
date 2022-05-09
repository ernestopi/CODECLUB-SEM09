# desafio: variáveis e loops
from turtle import *
lados = 8
angulo = 360 / lados
shape('turtle')
speed(8)
pensize(3)
color('red')

for count in range(36):
    forward(100)
    right(angulo)

done()