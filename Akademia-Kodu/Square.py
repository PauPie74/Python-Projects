import turtle as t
#żeby skracać

t.color('red')
t.hideturtle() #chowa strzałkę
t.pensize(20)
t.fillcolor('blue')
t.begin_fill()

for i in range (1,5):
    t.forward(60)
    t.left(90)

t.end_fill()

t.exitonclick() #działanie exit obsługuje

