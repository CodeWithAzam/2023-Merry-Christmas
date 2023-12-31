from turtle import *
from random import randint
import random


def create_rectangle(turtle,color,x,y,width,height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90) 
    
    turtle.end_fill()
    
    turtle.setheading(0)
    
def create_circle(turtle,x,y,radius,color):
    tr.penup()
    tr.color(color)
    tr.goto(x,y)
    tr.pendown()
    tr.fillcolor(color)
    tr.begin_fill()
    tr.circle(radius)
    tr.end_fill()
        
BG_COLOR='black'

tr=Turtle()

tr.speed(2)
screen=tr.getscreen()

screen.bgcolor(BG_COLOR)

screen.title("MERRY CHRISTMAS 2023")

screen.setup(width=1.0,height=1.0)

y = -100

create_rectangle(tr,'red',-15, y-60,30,60)

width=240
tr.speed(20)
while width>10:
    width=width-10
    height=10
    x=0-width/2
    create_rectangle(tr,"green",x,y,width,height)
    y=y+height
    
    
tr.speed(1)
tr.penup()
tr.color('yellow')
tr.goto(-20, y+10)
tr.begin_fill()
tr.pendown()
for i in range(5):
    tr.forward(40)
    tr.right(144)
tr.end_fill()

tr.penup()
tr.goto(20,60)
tr.color("yellow")
tr.circle(10)
tr.begin_fill()
tr.end_fill()

tr.goto(-40,20)
tr.color("red")
tr.begin_fill()
tr.circle(15)
tr.end_fill()

tr.goto(30,-20)
tr.color("orange")
tr.begin_fill()
tr.circle(10)
tr.end_fill()

tr.goto(85,-80)
tr.color("white")
tr.begin_fill()
tr.circle(20)
tr.end_fill()

tr.goto(-30,-40)
tr.color("blue")
tr.begin_fill()
tr.circle(15)
tr.end_fill()

tr.goto(-100,-100)
tr.color("yellow")
tr.begin_fill()
tr.circle(20)
tr.end_fill()

tree_height=y+40


create_circle(tr,230,180,60,"white")

create_circle(tr,220,180,60,BG_COLOR)


tr.speed(10)
number_of_stars= randint(20,30)
for _ in range(0,number_of_stars):
    x_star=randint(-(screen.window_width()//2),screen.window_width()//2)
    y_star=randint(tree_height, screen.window_height()//2)
    size=randint(5,20)
    tr.penup()
    tr.color('white')
    tr.goto(x_star,y_star)
    tr.begin_fill()
    tr.pendown()
    for i in range(5):
        tr.forward(size)
        tr.right(144)
    tr.end_fill()
    
    
tr.speed(1)
tr.penup()

msg1=""
msg2="MERRY CHRISTMAS 2023"
tr.goto(0,-200)
tr.color("white")
tr.write(msg1, move=False, align="center", font=("Arial",35,"bold"))
tr.goto(0,-300)
tr.color("white")

tr.write(msg2, move=False, align="center", font=("Arial",50,"bold"))

tr.hideturtle()
screen.mainloop()