import turtle
kushal_turtle=turtle.Turtle()
kushal_turtle.speed(6)
x=turtle.Screen()
kushal_turtle.begin_fill()


def square():
    kushal_turtle.forward(100)
    kushal_turtle.color("red","green")
    x.bgcolor("black")


    #kushal_turtle.fillcolor("orange")
    kushal_turtle.right(90)
    kushal_turtle.forward(200)
    kushal_turtle.right(90)
    kushal_turtle.forward(100)
    kushal_turtle.right(90)
    kushal_turtle.forward(200)
    kushal_turtle.right(90)
    kushal_turtle.forward(100)

    kushal_turtle.right(90)
    kushal_turtle.forward(70)
    kushal_turtle.left(90)
    kushal_turtle.forward(100)
    kushal_turtle.right(90)
    kushal_turtle.forward(50)
    kushal_turtle.right(90)
    kushal_turtle.forward(100)
    kushal_turtle.forward(200)
    kushal_turtle.right(90)
    kushal_turtle.forward(50)
    kushal_turtle.right(90)
    kushal_turtle.forward(200)
    kushal_turtle.backward(30)

    kushal_turtle.fillcolor("white")

    kushal_turtle.end_fill()

    kushal_turtle.hideturtle()

print(square())
print(help(turtle.speed))
