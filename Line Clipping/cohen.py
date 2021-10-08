import turtle as t

screen = t.Screen()
p = t.Turtle()
p.shapesize(0.1)
p.speed("fastest")
p.shape("circle")

xmin = -100
ymin = -100
xmax = 100
ymax = 100

p.penup()
p.goto(xmin, ymin)
p.pendown()
p.goto(xmin, ymax)
p.goto(xmax, ymax)
p.goto(xmax, ymin)
p.goto(xmin, ymin)
p.penup()
rej = 0  # Number of rejected lines


def tbrl(x, y):
    c = 0
    if y > ymax:  # Top part 1xyz
        c = 8
    if y < ymin:  # Bottom part x1yz
        c = 4
    if x > xmax:  # Right part xy1z
        c += 2
    if x < xmin:  # Left part xyz1
        c += 1

    return c


def cohen_line(x1, y1, x2, y2):
    c1 = tbrl(x1, y1)
    c2 = tbrl(x2, y2)
    m = (y2 - y1) / (x2 - x1)  # slope of the line
    accept = True

    while c1 | c2 > 0:  # until line is completely inside the window
        if c1 & c2 > 0:  # line is completely outside the window
            accept = False
            break

        xi = x1
        yi = y1
        c = c1

        if c == 0:  # first endpoint of the line is inside the window
            # we will shift to second end point of line
            c = c2
            xi = x2
            yi = y2

        x = 0.0
        y = 0.0

        if c & 8 > 0:  # end point is above the window viewport
            y = ymax  # clipping the upper part of the line
            x = xi + 1.0 / m * (ymax - yi)

        elif c & 4 > 0:  # line is below the window viewport
            y = ymin  # clipping the lower part of the line
            x = xi + 1.0 / m * (ymin - yi)

        elif c & 2 > 0:  # Line is in the right part
            x = xmax  # clipping the right part of the line
            y = yi + m * (xmax - xi)

        elif c & 1 > 0:  # Line is in the left part
            x = xmin  # clipping the left part of the line
            y = yi + m * (xmin - xi)

        if c == c1:  # We clipped the line for the first endpoint
            # Changing the first point
            x1 = x
            y1 = y
            c1 = tbrl(x1, y1)

        else:
            # changing 2nd endpoint
            x2 = x
            y2 = y

            c2 = tbrl(x, y)

    if accept:
        p.goto(x1, y1)
        p.pendown()
        p.goto(x2, y2)
        p.penup()

    else:
        global rej
        rej += 1
        p.goto(xmin - 30, ymin - 20 * rej)
        p.write(f"Line Rejected with end points: ({x1}, {y1}) and ({x2}, {y2})")


cohen_line(-50, -150, 150, 150)
cohen_line(-50, -150, 150, -150)
cohen_line(50, 150, 150, -150)
cohen_line(25, 50, 80, 90)

screen.exitonclick()
