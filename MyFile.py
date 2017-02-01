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
    wn.exitonclick()

DrawRectangle("Bob", 150, 120)
