#TurtleGraphics.py
#Name: Owen Betts
#Date: 02.16.2025
#Assignment: Practical Scripting Lab 4 

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)
              
#def fillCorner(alice, corner):
    drawSquare(alice, 100)
    
    if corner == 1:
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 2:
        alice.right(90)
        alice.forward(50)
        alice.left(90)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
        

def main():
    myTurtle = turtle.Turtle()

    
    
    
    #drawSquare(myTurtle, 100)
    
    # drawPolygon(myTurtle, 5) #draws a pentagon
    
    # drawPolygon(myTurtle, 8) #draws an octogon
    
    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.

    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares

def squaresInSquares(brock, size):
    drawSquare(brock, 200)
    brock.up()
    brock.goto(5, -5)
    brock.down()
    drawSquare(brock, 190)
    brock.up()
    brock.goto(-10, 10)
    brock.down()
    drawSquare(brock, 180)
    brock.up()
    brock.goto(-15, 15)
    brock.down()
    drawSquare(brock, 170)
    brock.up()
    brock.goto(-20, 20)
    brock.down()
    drawSquare(brock, 160)
        
    

    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
