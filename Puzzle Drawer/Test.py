# import turtle
# import string
# import time

# Columns = 5
# Rows = 5
# Width = (Columns*200)
# Height = (Rows*200)
# Alphabet = list(string.ascii_uppercase)
# UsedLetters = Alphabet[:(Columns*Rows)]

# def DrawSquare(x):
#     turtle.pendown()
#     offsetx = 60
#     offsety = 60
#     for i in range(0,4):
#         turtle.forward(180)
#         turtle.right(90)
#     turtle.penup()
#     turtle.goto( turtle.pos() + (30,-88))
#     turtle.left(90)
#     turtle.pendown()
#     DrawArrow()
#     turtle.penup()
#     turtle.goto( turtle.pos() + (offsetx, offsety))
#     turtle.left(180)
#     turtle.pendown()
#     DrawArrow()
#     turtle.penup()
#     turtle.goto( turtle.pos() + (offsety, -offsetx))
#     turtle.left(180)
#     turtle.pendown()
#     DrawArrow()
#     turtle.penup()
#     turtle.goto( turtle.pos() + (-offsetx, -offsety))
#     turtle.left(180)
#     turtle.pendown()
#     DrawArrow()
#     turtle.penup()
#     turtle.goto( turtle.pos() + (-20, -3))
#     turtle.write("0",align="center", font=("Arial", 20, "normal"))
#     turtle.goto( turtle.pos() + (-26, 70))
#     turtle.write("0",align="center", font=("Arial", 20, "normal"))
#     turtle.goto( turtle.pos() + (70, 22))
#     turtle.write("0",align="center", font=("Arial", 20, "normal"))
#     turtle.goto( turtle.pos() + (24, -70))
#     turtle.write("0",align="center", font=("Arial", 20, "normal"))
#     turtle.goto( turtle.pos() + (-45, 21))
#     turtle.write("A",align="center", font=("Arial", 20, "normal"))
#     turtle.left(90)

# def DrawArrow():
#     turtle.forward(40)
#     turtle.left(90)
#     turtle.forward(15)
#     turtle.right(135)
#     turtle.forward(40)
#     turtle.right(90)
#     turtle.forward(40)
#     turtle.right(135)
#     turtle.forward(15)
#     turtle.left(90)
#     turtle.forward(40)
#     turtle.right(90)
#     turtle.forward(27)



# def DrawGrid(Columns, Rows, LetterData):
#     f=0
#     x=0
#     y=0
#     for Row in range(0,Rows):
#         for Column in range(0,Columns):
#             turtle.goto((-((Width/2)-10)+(x*200)), ((Height/2)-10-(y*200)))
#             DrawSquare(LetterData[f])
#             x+=1
#         y+=1
#         x=0

# turtle.speed(100)
# turtle.setup(Width,Height)
# turtle.penup()
# turtle.goto(-((Width/2)-10), ((Height/2)-10))
# turtle.pendown()
# turtle.pensize(3)

# DrawGrid(Columns, Rows, "hey")
# turtle.done() 




