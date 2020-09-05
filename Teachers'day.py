import turtle as ku
import random as rn

ku.color('pink')
style=('blue',20,'bold')
ku.write("From:Kushal \n\n\n\n\n\n\n\n ",font=style,align='right')

ku.color('red')
style1=('blue',20,'bold')
ku.write("Happy Teacher’s Day!\n\n\n\n\n\n ",font=style1,align='left')


ku.color('orange')
style3=('blue',20,'bold')
ku.write("Thanks for being my best Teacher!\n\n\n\n ",font=style3,align='center')

ku.color('magenta')
style1=('blue',20,'bold')
ku.write("Thank You!\n\n ",font=style1,align='left')


ku.color('green')
style2=('blue',17,'bold')
ku.write("“Let us remember: One book, one pen, one child, and one teacher can change the world.” –Malala Yousafzai ",font=style2,align='center')
def star(x,y,color,side):
    ku.color(color)
    ku.begin_fill()
    ku.penup()
    ku.goto(x,y)
    ku.pendown()
    for i in range(5):
        ku.forward(side)
        ku.right(144)
        ku.forward(side)
    ku.end_fill()

def random_length():
    return rn.randrange(5,25)
def random_color():
    return rn.randrange(-590,590),rn.randrange(-570,570)
ku.title("Teacherday")
ku.bgcolor("black")
ku.speed(0)
colors=['red','orange','magenta','green','blue','yellow']
stars=100
for i in range(stars):
    color=rn.choice(colors)
    side=random_length()
    x,y=random_color()
    star(x,y,color,side)
ku.end_fill()

ku.hideturtle()
ku.done()
