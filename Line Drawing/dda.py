# ------------------------------------ Library Imports -------------------------------------------- #
import turtle as t


# --------------------------------------- User Input ----------------------------------------------- #
x1, y1 = map(float, (input("please enter the  coordinate of starting point: ")).split())
x2, y2 = map(float, (input("please enter the  coordinate of starting point: ")).split())


# ---------------------------- turtle and screen configuration ------------------------------------ #
screen = t.Screen()
point = t.Turtle()
point.shapesize(0.01)
point.speed("slowest")
point.shape("circle")


# -------------------------------------- DDA ALGORITHM ---------------------------------------------- #
dx = x2 - x1
dy = y2 - y1

steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
steps = int(steps)

x_change = dx / steps
y_change = dy / steps

point.penup()
point.goto(int(x1), int(y1))
point.pendown()

x1 += 0.5
y1 += 0.5

for i in range(steps):
    x1 += x_change
    y1 += y_change

    point.goto(int(x1), int(y1))

screen.exitonclick()
