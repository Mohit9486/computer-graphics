# ------------------------------------ Library Imports -------------------------------------------- #
import turtle as t

# --------------------------------------- User Input ----------------------------------------------- #
n = int(input("Please Enter the number of sides of polygon: "))
points = []

for i in range(n):
    x, y = map(float, input("Please enter the point " + str(i + 1) + ": ").split())
    points.append((x, y))


# ---------------------------- turtle and screen configuration ------------------------------------ #
screen = t.Screen()
point = t.Turtle()
point.shapesize(0.01)
point.pensize(1)
point.speed("fastest")
point.shape("circle")
point.color("black")
point.penup()
point.shapesize(0.1)


# DDA Algorithm to get boundary points
boundary_points = set()
isFirstSide = True  # to get seed point
first_side = []


def create_line(x1, y1, x2, y2):
    global isFirstSide
    dx = x2 - x1
    dy = y2 - y1

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    steps = int(steps)

    x_change = dx / steps
    y_change = dy / steps

    boundary_points.add((int(x1), int(y1)))
    point.goto(int(x1), int(y1))
    point.dot()
    first_side.append((int(x1), int(y1)))

    x1 += 0.5
    y1 += 0.5

    for _ in range(steps):
        x1 += x_change
        y1 += y_change

        boundary_points.add((int(x1), int(y1)))
        point.goto(int(x1), int(y1))
        point.dot()
        if f:
            first_side.append((int(x1), int(y1)))

    f = False


# ------------------------------------ Seed Point calculator -------------------------------------------- #
def helper(x1, y1, b, x2=-1000, y2=-1000):
    c = 0
    dx = x2 - x1
    dy = y2 - y1

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    steps = int(steps)

    x_change = dx / steps
    y_change = dy / steps

    x1 += 0.5
    y1 += 0.5

    for _ in range(steps):
        x1 += x_change
        y1 += y_change

        if (int(x1), int(y1)) in b:
            c += 1

    return c % 2 == 1


def seed_point(side, boundary):
    for p in side:
        if helper(p[0], p[1] + 1, boundary):
            return p[0], p[1] + 1
        if helper(p[0], p[1] - 1, boundary):
            return p[0], p[1] - 1

        if helper(p[0] + 1, p[1], boundary):
            return p[0] + 1, p[1]
        if helper(p[0] - 1, p[1], boundary):
            return p[0] - 1, p[1]

    return -1000, -1000


def fill_4connected(x1, y1):
    if (x1, y1) in boundary_points:
        return

    vis = {(x1, y1)}

    q = [(x1, y1)]

    while len(q) > 0:
        x1, y1 = q.pop(0)

        point.goto(x1, y1)
        point.dot()
        if ((x1 + 1, y1) not in boundary_points) and ((x1 + 1, y1) not in vis):
            q.append((x1 + 1, y1))
            vis.add((x1 + 1, y1))
        if ((x1 - 1, y1) not in boundary_points) and ((x1 - 1, y1) not in vis):
            q.append((x1 - 1, y1))
            vis.add((x1 - 1, y1))
        if ((x1, y1 + 1) not in boundary_points) and ((x1, y1 + 1) not in vis):
            q.append((x1, y1 + 1))
            vis.add((x1, y1 + 1))
        if ((x1, y1 - 1) not in boundary_points) and ((x1, y1 - 1) not in vis):
            q.append((x1, y1 - 1))
            vis.add((x1, y1 - 1))


# --------------------------------------- creating boundary ----------------------------------------------- #
for i in range(1, n):
    create_line(points[i - 1][0], points[i - 1][1], points[i][0], points[i][1])

create_line(points[0][0], points[0][1], points[n - 1][0], points[n - 1][1])

# --------------------------------------- Seed Point ----------------------------------------------- #
x = seed_point(first_side, boundary_points)

# --------------------------------------- Flood fill ----------------------------------------------- #
point.color("red")
if x[0] != -1000:
    fill_4connected(x[0], x[1])


else:
    print("couldn't find interior point")


screen.exitonclick()
