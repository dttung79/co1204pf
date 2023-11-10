# Write a program that draws n squares of multiple random colors.
# All squares are of the same size and moving around a corner (top left corner).
# The program will ask for n, then draw n squares.
import turtle as t
import random as rd
t.speed(0)

t.colormode(255)

n = int(input('Enter n: '))

for i in range(n):
    # draw a square
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    t.color(r, g, b)
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.left(360/n)

t.exitonclick()