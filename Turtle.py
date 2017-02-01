"""Create a Turtle Program that will draw a 3-dimensional cube"""

import turtle
hi = turtle.Turtle()
wn = turtle.Screen()
for i in range(4):
    hi.fd(50)
    hi.left(90)
hi.goto(20,20)
for i in range(4):
    hi.fd(50)
    hi.left(90)
hi.pu()
hi.goto(50,0)
hi.pd()
hi.goto(70,20)
hi.pu()
hi.goto(50,50)
hi.pd()
hi.goto(70,70)
hi.pu()
hi.goto(0,50)
hi.pd()
hi.goto(20,70)
wn.exitonclick()


"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""
