import turtle
import string
import random

Columns = 4
Rows = 4
Width = (Columns*200)
Height = (Rows*200)
Alphabet = list(string.ascii_uppercase)
UsedLetters = Alphabet[:(Columns*Rows)]

class PuzzleBoxes:
    def __init__(self, Column, Row, Letter, Up=0, Right=0, Down=0, Left=0):
        self.Column = Column
        self.Row = Row
        self.Letter = Letter
        self.Up = Up
        self.Right = Right
        self.Down = Down
        self.Left = Left

def Shuffle(UsedLetters):
    return random.sample(UsedLetters, len(UsedLetters))

def CalculatePosition(Letter, Columns, Rows, UsedLetters):
    LetterPosition = UsedLetters.index(Letter)
    LetterColumn = LetterPosition%Columns
    LetterRow = LetterPosition//Columns
    # print(LetterColumn, LetterRow)
    return LetterColumn, LetterRow

def CalculateMovement(FromLetter, ToLetter, Columns, Rows, UsedLetters):
    FromLetterColumn, FromLetterRow = CalculatePosition(FromLetter, Columns, Rows, UsedLetters)
    ToLetterColumn, ToLetterRow = CalculatePosition(ToLetter, Columns, Rows, UsedLetters)
    ColumnDisplacement = FromLetterColumn - ToLetterColumn
    RowDisplacement = FromLetterRow - ToLetterRow
    if ColumnDisplacement >= 0:
        Left = ColumnDisplacement
        Right = 0
    else:
        Left = 0
        Right = -ColumnDisplacement
    if RowDisplacement >= 0:
        Up = RowDisplacement
        Down = 0
    else:
        Up = 0
        Down = -RowDisplacement

    return Up, Right, Down, Left



ShuffledLetters = Shuffle(UsedLetters)
CalculateMovement("B", "G", Columns, Rows, UsedLetters)
print()

LetterData = []
for Letter in UsedLetters:
    LetterPosition = ShuffledLetters.index(Letter)
    if LetterPosition == 0:
        LetterData.append(PuzzleBoxes(*CalculatePosition(Letter, Columns, Rows, UsedLetters), Letter))
    else:
        LetterData.append(PuzzleBoxes(*CalculatePosition(Letter, Columns, Rows, UsedLetters), Letter, *CalculateMovement(Letter, ShuffledLetters[LetterPosition-1], Columns, Rows, UsedLetters)))
print()

#-------------------TERRIBLE CODE AHEAD -------------------

def DrawSquare(PuzzleBoxData):
    turtle.pendown()
    offsetx = 60
    offsety = 60
    for i in range(0,4):
        turtle.forward(180)
        turtle.right(90)
    turtle.penup()
    turtle.goto( turtle.pos() + (30,-88))
    turtle.left(90)
    turtle.pendown()
    DrawArrow()
    turtle.penup()
    turtle.goto( turtle.pos() + (offsetx, offsety))
    turtle.left(180)
    turtle.pendown()
    DrawArrow()
    turtle.penup()
    turtle.goto( turtle.pos() + (offsety, -offsetx))
    turtle.left(180)
    turtle.pendown()
    DrawArrow()
    turtle.penup()
    turtle.goto( turtle.pos() + (-offsetx, -offsety))
    turtle.left(180)
    turtle.pendown()
    DrawArrow()
    turtle.penup()
    turtle.goto( turtle.pos() + (-20, -3))
    turtle.write(PuzzleBoxData.Left,align="center", font=("Arial", 20, "normal"))
    turtle.goto( turtle.pos() + (-26, 70))
    turtle.write(PuzzleBoxData.Up,align="center", font=("Arial", 20, "normal"))
    turtle.goto( turtle.pos() + (70, 22))
    turtle.write(PuzzleBoxData.Right,align="center", font=("Arial", 20, "normal"))
    turtle.goto( turtle.pos() + (24, -70))
    turtle.write(PuzzleBoxData.Down,align="center", font=("Arial", 20, "normal"))
    turtle.goto( turtle.pos() + (-45, 21))
    turtle.write(PuzzleBoxData.Letter,align="center", font=("Arial", 20, "normal"))
    turtle.left(90)

def DrawArrow():
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(135)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(135)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(27)



def DrawGrid(Columns, Rows, LetterData):
    f=0
    x=0
    y=0
    for Row in range(0,Rows):
        for Column in range(0,Columns):
            turtle.goto((-((Width/2)-10)+(x*200)), ((Height/2)-10-(y*200)))
            DrawSquare(LetterData[f])
            f+=1
            x+=1
        y+=1
        x=0

turtle.speed(20)
turtle.setup(Width,Height)
turtle.penup()
turtle.goto(-((Width/2)-10), ((Height/2)-10))
turtle.pendown()
turtle.pensize(3)

DrawGrid(Columns, Rows, LetterData)
turtle.done()
print()