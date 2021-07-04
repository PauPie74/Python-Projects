import turtle as t

t.hideturtle()

#Przepis na ciasto

def draw_circle(x,y,color):
    t.pensize(10)
    t.color(color)
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.circle(30)

draw_circle (60,0,'blue')
draw_circle (-15,0,'purple')
draw_circle (90,40,'red')
draw_circle (15,40,'yellow')
draw_circle (-60,40,'green')