import turtle
kushal_turtle=turtle.Turtle()
kushal_turtle.speed(1)

def square():
    kushal_turtle.forward(100)
    kushal_turtle.right(90)
    kushal_turtle.forward(100)
    kushal_turtle.right(90)
    kushal_turtle.forward(100)
    kushal_turtle.right(90)
    kushal_turtle.forward(100)

for count in range(4):
    kushal_turtle.color("red","green")
    square()
