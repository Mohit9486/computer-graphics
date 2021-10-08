# ------------------------------------ Library Imports -------------------------------------------- #
import turtle as t


# --------------------------------------- User Input ----------------------------------------------- #
x1, y1 = map(int, (input("please enter the  coordinate of center: ")).split())
radius = float(input("Please enter the length of the radius of the circle: "));

# ---------------------------- turtle and screen configuration ------------------------------------ #
screen = t.Screen()
point = t.Turtle()
# point.shapesize(0.1)
# point.speed("slowest")
point.pencolor("red")

point.penup()
point.goto(x1, y1)
point.pendown()
point.dot()
point.write("C")

point.shape("arrow")
point.pencolor("blue")
point.penup()

# -------------------------------------- Information about circle ---------------------------------------------- #

# equation of circle ( center at origin) : x**2 + y**2 = r**2
# if center is x1, y1 then by origin shift the circle equation will be: (x - x1)**2 + (y - y1)**2 = r**2
# any point which has coordinates (x2, y2) in the circle at origin then in the shifted circle the
# coordinates will be (x1 + x2, y1 + y2)


# -------------------------------------- Mid Point ALGORITHM ---------------------------------------------- #

# we will start plotting circle from the point(0, r) i.e. (x1, y1 + r)
x = 0
y = round(radius)

# decision parameter
p = 5 / 4 - radius

# we will until we don't reach at point where x != y (when center is origin) and in general till x1 - x ! = y1 - y


def plot_point(xc, yc):
    point.goto(xc, yc)
    point.dot()


while x <= y:
    plot_point(x + x1, y + y1)
    plot_point(y + x1, x + y1)
    plot_point(-y + x1, x + y1)
    plot_point(-x + x1, y + y1)
    plot_point(x + x1, -y + y1)
    plot_point(y + x1, -x + y1)
    plot_point(-y + x1, -x + y1)
    plot_point(-x + x1, -y + y1)

    if p < 0:
        p = p + 2 * x + 1

    else:
        p = p + 2 * x + 1 - 2 * y
        y -= 1

    x += 1

screen.exitonclick()
