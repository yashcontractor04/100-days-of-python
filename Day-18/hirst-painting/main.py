import random
import turtle as t

# RGB color palette extracted from Damien Hirst spot paintings
color_list = [(204, 164, 107), (155, 73, 46), (235, 238, 244), (52, 92, 123), (224, 201, 135), (171, 153, 40), (138, 31, 21), (132, 162, 185), (200, 91, 71), (48, 122, 87), (14, 99, 73), (95, 73, 75), (146, 178, 147), (72, 47, 38), (163, 142, 158), (234, 175, 165), (55, 46, 50), (184, 206, 172), (19, 85, 90), (144, 21, 24), (41, 62, 74), (82, 145, 128), (181, 87, 89), (41, 66, 90), (13, 71, 68), (213, 178, 183), (179, 191, 207)]

tim = t.Turtle()
screen = t.Screen()

# Configure RGB 0-255 mode for custom tuple colors
t.colormode(255)

def pain_hirst_row():
    tim.speed(4)
    tim.pensize(20)
    for i in range(10):
        tim.pencolor(random.choice(color_list))
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

def pain_hirst():
    screen.setworldcoordinates(25, 25, 500, 500)
    screen.bgcolor()
    tim.pu()
    tim.hideturtle()
    for _ in range(10):
        # Reposition turtle to the start of the next row
        tim.teleport(25, tim.ycor() + 50)
        pain_hirst_row()


pain_hirst()

screen.exitonclick()
