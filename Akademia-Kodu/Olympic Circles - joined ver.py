import turtle as t

t.color('lime')
t.hideturtle() #chowa strzałkę
t.pensize(10)

t.circle(30)

#turtle.pendown()
#turtle.pd()
#turtle.down()
#   Pull the pen down – drawing when moving.

#turtle.penup()
#turtle.pu()
#turtle.up()¶
#   Pull the pen up – no drawing when moving.

t.penup()
t.setposition(60,0)

t.pendown()
t.color('yellow')
t.circle(30)

t.setposition(120,0)
t.color('red')
t.circle(30)

t.setposition(90,-50)
t.color('blue')
t.circle(30)

t.setposition(30,-50)
t.color('purple')
t.circle(30)

t.exitonclick() #działanie exit obsługuje

