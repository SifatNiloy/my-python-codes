import turtle
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
turtle.speed(0)
turtle.penup()
turtle.backward(300)
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.pen(pencolor="green", fillcolor="green", pensize=3, speed=2)
turtle.pendown()
turtle.begin_fill()
for i in range(2):
    turtle.forward(600)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
turtle.end_fill()
turtle.speed(5)
turtle.penup()
turtle.forward(400)
turtle.left(90)
turtle.forward(200)
turtle.pendown()
turtle.pen(pencolor="red", fillcolor="red", pensize=3, speed=2)
turtle.begin_fill()
turtle.circle(130)
turtle.end_fill()
turtle.speed(10)
turtle.left(90)
turtle.forward(20)

turtle.exitonclick()