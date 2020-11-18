# code my Nitin Sain
import turtle
diwali = turtle.Screen()
diwali.bgcolor("black")
turtle = turtle.Turtle()
turtle.shape("arrow")
turtle.color("black")
turtle.width(7)
colors = ["peru", "ivory", "dark orange", "coral", "cyan", "hot pink", "gold", "ivory", "yellow", "red", "pink",
          "green", "blue", "light blue", "light green", ]

def star():
     turtle.width(2)
     turtle.speed(40)
     for i in range(8):
         turtle.fd(50)
         turtle.lt(225)


def Deep():
    turtle.color("orange")
    turtle.width(4)
    turtle.speed(1)
    turtle.left(90)
    turtle.forward(300)
    turtle.goto(40,-250)
    turtle.right(180)
    turtle.forward(40)
    turtle.goto(200, -150)
    turtle.fillcolor("orange")
    turtle.circle(50,180)
    turtle.circle(50, 180)
    turtle.fillcolor("gold")





def draw_happy(i, x, y):
    turtle.pencolor("linen")
    turtle.color(colors[i % 7])
    turtle.begin_fill()
    turtle.lt(70)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(33)
    turtle.end_fill()


def move(x, y):
    turtle.up()
    turtle.setposition(0, 0)
    turtle.setheading(90)
    turtle.rt(90)
    turtle.fd(x)
    turtle.lt(90)
    turtle.fd(y)
    turtle.pendown()


def mov(x, y):
    turtle.up()
    turtle.setposition(0, 0)
    turtle.setheading(90)
    turtle.lt(90)
    turtle.fd(x)
    turtle.rt(90)
    turtle.fd(y)
    turtle.pendown()


def A(size):
    turtle.rt(19)
    turtle.forward(size)
    turtle.rt(141)
    turtle.fd(size)
    turtle.backward(size / 2)
    turtle.rt(105)
    turtle.fd(int(size / 3))



def D(size):
    turtle.fd(size)
    turtle.rt(90)
    turtle.fd(size // 10)
    for i in range(13):
        turtle.rt(13)
        turtle.fd(size // 8)

def H(size):
    turtle.fd(size)
    turtle.backward(size // 2)
    turtle.rt(90)
    turtle.fd(size // 2)
    turtle.lt(90)
    turtle.fd(size // 2)
    turtle.backward(size)


def I(size):
    turtle.fd(size)
    turtle.rt(90)
    turtle.circle(size // 8)



def L(size):
    turtle.rt(90)
    turtle.fd(int(size / 2))
    turtle.back(int(size / 2))
    turtle.lt(90)
    turtle.fd(size)




def P(size):
    turtle.fd(size)
    turtle.rt(90)
    turtle.fd(size // 8)
    for i in range(8):
        turtle.rt(20)
        turtle.fd(size // 9)


def W(size):
    turtle.lt(20)
    turtle.fd(size)
    turtle.back(size)
    turtle.rt(50)
    turtle.fd(size // 1.5)
    turtle.lt(60)
    turtle.backward(size // 1.5)
    turtle.rt(50)
    turtle.fd(size)

def Y(size):
    turtle.fd(size)
    turtle.left(60)
    turtle.fd(size // 2)
    turtle.backward(size // 2)
    turtle.rt(90)
    turtle.fd(size // 1.5)





# Name section
turtle.speed(10)
turtle.width(15)
# happybithday
turtle.pencolor("cyan")
turtle.width(13)
mov(260, 0)
H(100)
turtle.width(7)
mov(190, 0)
A(65)
mov(135, 0)
P(60)
mov(100, 0)
P(60)
mov(52, 0)
Y(60)
move(20, 0)
turtle.pencolor('gold')
D(200)
move(170, 0)
I(60)
move(230, 0)
W(60)
move(300, 0)
A(65)
move(370, 0)
L(65)
move(420, 0)
I(60)
move(400, -150)

# stars
turtle.color("gold")
star()
move(300,200)
turtle.color("blue")
star()
move(-200,-200)
turtle.color("pink")
star()
move(-400,-200)
turtle.color("ivory")
star()
move(-400,210)
turtle.color("white")
star()
move(-200,210)
turtle.color("red")
star()
move(-300,200)
turtle.color("pink")
star()
move(-100,150)
turtle.color("gold")
star()
move(400,150)
turtle.color("pink")
star()
move(500,-100)
turtle.color("pink")
star()
move(-400,50)
turtle.color("gold")
star()
move(180,270)
turtle.color("gold")
star()
move(-300,-300)
turtle.color("gold")
star()
move(170,-150)
Deep()
