import turtle as t


x1 = int(input("X coordinate of center: "))
y1 = int(input("y coordinate of center: "))
r = float(input("Radius: "))

screen = t.Screen()
p = t.Turtle()
p.speed("fastest")
p.penup()
p.goto(x1, y1)
p.dot()
p.pendown()
p.pencolor("red")
p.write("center")
p.penup()

x = 0
y = round(r)
D = 5 / 4 - r

while x <= y:
    p.goto(x + x1, y + y1)
    p.dot()
    p.goto(y + x1, x + y1)
    p.dot()
    p.goto(-y + x1, x + y1)
    p.dot()
    p.goto(-x + x1, y + y1)
    p.dot()
    p.goto(x + x1, -y + y1)
    p.dot()
    p.goto(y + x1, -x + y1)
    p.dot()
    p.goto(-y + x1, -x + y1)
    p.dot()
    p.goto(-x + x1, -y + y1)
    p.dot()

    if D < 0:
        D = D + 2 * x + 1

    else:
        D = D + 2 * x + 1 - 2 * y
        y -= 1

    x += 1

screen.exitonclick()
