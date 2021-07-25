# https://docs.python.org/3/library/turtle.html
# https://realpython.com/beginners-guide-python-turtle/

import turtle as t

x = t.Turtle()

t.bgcolor("blue")

t.right(90)
t.forward(100)
t.left(90)
t.backward(100)
t.goto(100,100)
t.home()

#Square
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

#Circle
t.circle(60)

t.dot(20)

t.bgcolor("yellow")

t.title("My Turtle Program")

t.shapesize(1,5,10)
t.shapesize(10,5,1)
t.shapesize(1,10,5)
t.shapesize(10,1,5)

t.pensize(5)
t.forward(100)

t.shapesize(3,3,3)

t.fillcolor("red")

t.pencolor("green")
t.color("green", "red")

t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()

t.shape("turtle")
t.shape("arrow")
t.shape("circle")

t.speed(1)
t.forward(100)
t.speed(10)
t.forward(100)