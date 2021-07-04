import turtle as t

t.color('red')
t.hideturtle() #chowa strzałkę
t.pensize(10)

#for i in range (1,40):
#    t.forward(10)
#    t.left(10)
#very nice wyszło xDDD

#t.circle(40) #circle(radius)

r = 10

n = 10

for i in range (1, n + 1, 1):
    t.circle(r*i)

t.exitonclick() #działanie exit obsługuje

