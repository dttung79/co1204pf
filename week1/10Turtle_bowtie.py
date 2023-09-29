# draw a bowtie

import turtle as t

t.pensize(3)

# draw the 1st square in red
t.fillcolor('red')
t.begin_fill()
t.goto(100, 0)
t.goto(100, 100)
t.goto(0, 100)
t.goto(0, 0)
t.end_fill()

# draw the 2nd square in blue
t.fillcolor('blue')
t.begin_fill()
t.goto(-100, 0)
t.goto(-100, -100)
t.goto(0, -100)
t.goto(0, 0)
t.end_fill()

t.exitonclick()
