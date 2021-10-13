# Lab07Bst.py
# "Selection With Graphics"
# This is the student, starting version of Lab 07B.

from Graphics import *

beginGrfx(1300,700)

# Substitute your own name here.
drawHeading("Afshaal Zubair","7B")
# The center of the coordinate grid is 650,350.

shapeNum = numinput("Shape Selection", "1 = Line \n2 = Rectangle \n3 = Circle \n4 = Oval \n5 = Regular Octagon \n6 = Star \n7 = Burst")

if shapeNum == 1:
    shapeColor = textinput("Color Selection", "Enter any color name.")
    if type(shapeColor) == str:
        setColor(shapeColor)
        shapeWidth = numinput("Width Selection", "Enter 1-100")
        if shapeWidth in range(1, 101):
            width(shapeWidth)
            drawLine(400, 350, 800, 350)
        else:
            setColor("Black")
            drawString("Error... Please enter a width from 1-100.", 350, 350, "Arial", 24, "bold")
    else:
        drawString("Error... Please enter a valid color.", 350, 350, "Arial", 24, "bold")
elif shapeNum == 2:
    shapeColor = textinput("Color Selection", "Enter any color name.")
    if type(shapeColor) == str:
        setColor(shapeColor)
        shapeWidth = numinput("Width Selection", "Enter 1-100")
        if shapeWidth in range(1, 101):
            width(shapeWidth)
            drawRectangle(200, 200, 1100, 600)
        else:
            setColor("Black")
            drawString("Error... Please enter a width from 1-100.", 350, 350, "Arial", 24, "bold")
    else:
        drawString("Error... Please enter a valid color.", 350, 350, "Arial", 24, "bold")
elif shapeNum == 3:
    shapeColor = textinput("Color Selection", "Enter any color name.")
    if type(shapeColor) == str:
        setColor(shapeColor)
        shapeWidth = numinput("Width Selection", "Enter 1-100")
        if shapeWidth in range(1, 101):
            width(shapeWidth)
            drawCircle(650, 350, 200)
        else:
            setColor("Black")
            drawString("Error... Please enter a width from 1-100.", 350, 350, "Arial", 24, "bold")
    else:
        drawString("Error... Please enter a valid color.", 350, 350, "Arial", 24, "bold")
elif shapeNum == 4:
    shapeColor = textinput("Color Selection", "Enter any color name.")
    if type(shapeColor) == str:
        setColor(shapeColor)
        shapeWidth = numinput("Width Selection", "Enter 1-100")
        if shapeWidth in range(1, 101):
            width(shapeWidth)
            drawOval(650, 350, 400, 200)
        else:
            setColor("Black")
            drawString("Error... Please enter a width from 1-100.", 350, 350, "Arial", 24, "bold")
    else:
        drawString("Error... Please enter a valid color.", 350, 350, "Arial", 24, "bold")
elif shapeNum == 5:
    shapeColor = textinput("Color Selection", "Enter any color name.")
    if type(shapeColor) == str:
        setColor(shapeColor)
        shapeWidth = numinput("Width Selection", "Enter 1-100")
        if shapeWidth in range(1, 101):
            width(shapeWidth)
            drawRegularPolygon(650, 350, 200, 8)
        else:
            setColor("Black")
            drawString("Error... Please enter a width from 1-100.", 350, 350, "Arial", 24, "bold")
    else:
        drawString("Error... Please enter a valid color.", 350, 350, "Arial", 24, "bold")
elif shapeNum == 6:
    shapeColor = textinput("Color Selection", "Enter any color name.")
    if type(shapeColor) == str:
        setColor(shapeColor)
        shapeWidth = numinput("Width Selection", "Enter 1-100")
        if shapeWidth in range(1, 101):
            width(shapeWidth)
            drawStar(650, 350, 200, 5)
        else:
            setColor("Black")
            drawString("Error... Please enter a width from 1-100.", 350, 350, "Arial", 24, "bold")
    else:
        drawString("Error... Please enter a valid color.", 350, 350, "Arial", 24, "bold")
elif shapeNum == 7:
    shapeColor = textinput("Color Selection", "Enter any color name.")
    if type(shapeColor) == str:
        setColor(shapeColor)
        shapeWidth = numinput("Width Selection", "Enter 1-100")
        if shapeWidth in range(1, 101):
            width(shapeWidth)
            drawBurst(650, 350, 200, 20)
        else:
            setColor("Black")
            drawString("Error... Please enter a width from 1-100.", 350, 350, "Arial", 24, "bold")
    else:
        drawString("Error... Please enter a valid color.", 350, 350, "Arial", 24, "bold")
else:
    drawString("Error... Please enter a number from 1-7.", 350, 350, "Arial", 24, "bold")
        
endGrfx()