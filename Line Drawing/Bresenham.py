# ------------------------------------ Library Imports -------------------------------------------- #
import turtle as t

notDone = True

while notDone:  # To take user's input until he does not enter a valid input
    # --------------------------------------- Input Instructions ----------------------------------------------- #
    print("Please consider you give input such that:")
    print("-> Coordinates of starting point is less than the coordinates of ending point")
    print("-> Slope must be less than 1, i.e (y2 - y1) must be less than (x2 - x1)")

    # ------------------------------------------ User Inputs -------------------------------------------------- #
    x1, y1 = map(int, (input("please enter the  coordinate of starting point: ")).split())
    x2, y2 = map(int, (input("please enter the  coordinate of starting point: ")).split())

    dx = x2 - x1
    dy = y2 - y1

    if dy < 0 or dx < 0 or dy > dx:
        print("Please give the inputs according the instructions")

    else:
        # ---------------------------- turtle and screen configuration ------------------------------------ #
        screen = t.Screen()
        point = t.Turtle()
        point.shapesize(0.01)
        point.speed("slowest")
        point.shape("circle")

        # ------------------------------------- Bresenham ALGORITHM ----------------------------------------- #
        D = 2 * dy - dx

        point.penup()
        point.goto(x1, y1)
        point.pendown()

        for i in range(dx):
            x1 += 1
            if D < 0:
                D += 2 * dy

            else:
                D += 2 * dy - 2 * dx
                y1 += 1

            point.goto(x1, y1)

        notDone = False

        screen.exitonclick()
