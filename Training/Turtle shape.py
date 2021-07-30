import turtle as t

x = t.Turtle()

t.bgcolor("black")

t.pencolor("red")
x = 30

t.fillcolor("yellow")

for i in range(12):
    t.begin_fill()
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.home()
    t.rt(x)
    x += 30
    t.end_fill()

t.fillcolor("red")
t.fillcolor("red")

for i in range(12):
    t.begin_fill()
    t.fd(200)
    t.rt(45)
    t.fd(100)
    t.home()
    t.rt(x)
    x += 30
    t.end_fill()

#t.fillcolor("green")
#t.fillcolor("blue")

#t.penup()

#t.fd(25)
#t.begin_fill()
#t.circle(50)
#t.end_fill()