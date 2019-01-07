# Ch2 Exercise 3.13
# Macky Ruiz
# CIS 007

import turtle
turtle.pensize(3)
turtle.penup()
turtle.goto(50, -200)
turtle.setheading(22.5)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(200, steps = 8)
turtle.end_fill()

turtle.color("white")
turtle.penup()
turtle.goto(-160, -70)
turtle.pendown()
turtle.write("STOP",
    font = ("Times", 80, "bold"))
turtle.hideturtle()

turtle.done ()
