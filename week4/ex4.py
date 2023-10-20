import turtle as t

n = int(input('Enter n: '))
length = 100

angle = 360 / n

for i in range(n):
    t.forward(length)
    t.left(angle)

t.exitonclick()