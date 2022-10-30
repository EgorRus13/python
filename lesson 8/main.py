# import random as r
# from random import randint
# x=r.randint(0 , 100)
# lst = [0, 1, 2, 3, 4, 5]
# element_random=r.choice(lst)
# r.shuffle(lst)
#
# print(x)
# print(lst)
# print(element_random)
import turtle
tortoise=turtle.Turtle()
tortoise.shape("turtle")
tortoise.penup()
tortoise.goto(-350,300)
tortoise.pendown()
tortoise.color("green")
tortoise.pensize(10)
tortoise.speed(5)
screen=turtle.Screen()
tortoise.forward(310)
tortoise.right(90)
tortoise.forward(210)
tortoise.right(90)
tortoise.forward(310)
tortoise.right(90)
tortoise.forward(210)
tortoise.penup()
tortoise.goto(-180,200)
tortoise.pendown()
tortoise.right(90)
tortoise.forward(50)
tortoise.write("Movavi",font=("Arial Black",50,"normal"),align="center")


screen.exitonclick()