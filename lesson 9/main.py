import turtle
import random
screen=turtle.Screen()
t=turtle.Turtle()
t.pensize(15)
t.speed(2)
colors=["red","orange","yellow","green","light blue","blue","purple"]

side=int(input("Введи кол-во сторон: "))
x=80
for i in range(0,side):
    t.pencolor(random.choice(colors))
    t.fd(x)
    t.rt(360/side)

screen.exitonclick()