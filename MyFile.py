"""
AddTen Function
"""
def AddTen(n):
    return n + 10

x = 13
print(str(x) +" + 10 =" , str(AddTen(x)))


"""
DrawRectangle Function
"""
def DrawRectangle(AnyTurtle, l, w):
    import turtle
    AnyTurtle = turtle.Turtle()
    wn = turtle.Screen()
    for i in range(2):
        AnyTurtle.fd(l)
        AnyTurtle.left(90)
        AnyTurtle.fd(w)
        AnyTurtle.left(90)

DrawRectangle("Bob", 150, 120)


"""
DrawPoly Function
"""
def DrawPoly(AnyTurtle, n):
    import turtle
    AnyTurtle = turtle.Turtle()
    AnyTurtle.color("Lime Green")
    wn = turtle.Screen()
    wn.bgcolor("Black")
    wn.title("Shape Creator!")
    ang = (360/n)
    for i in range(n):
        AnyTurtle.fd(50)
        AnyTurtle.left(ang)
    wn.exitonclick()

DrawPoly("Bob II" , 8)
