import turtle, math
from math import pi,sin,cos


turtle.bgcolor("black")
turtle.setup(700,700)
turtle.pu()
turtle.ht()
turtle.setx(0)
turtle.sety(-266)
turtle.pd()
turtle.speed(100)
turtle.pencolor('red3')
turtle.begin_fill()
turtle.circle(266)
turtle.color('red3')
turtle.end_fill()



from turtle import Turtle

mbl1 = Turtle()
mbl1.shape('circle')
mbl1.color('red3')
mbl1.pu()
mbl1.color('white')
mbl1.shape('circle')
mbl1.turtlesize(1.5)
mbl1.left(180)

mbl2 = Turtle()
mbl2.shape('circle')
mbl2.color('red3')
mbl2.pu()
mbl2.color('white')
mbl2.shape('circle')
mbl2.turtlesize(1.5)
mbl2.left(180)

mbl3 = Turtle()
mbl3.shape('circle')
mbl3.color('red3')
mbl3.pu()
mbl3.color('white')
mbl3.shape('circle')
mbl3.turtlesize(1.5)
mbl3.left(180)

mbl4 = Turtle()
mbl4.shape('circle')
mbl4.color('red3')
mbl4.pu()
mbl4.color('white')
mbl4.shape('circle')
mbl4.turtlesize(1.5)

mbl5 = Turtle()
mbl5.shape('circle')
mbl5.color('red3')
mbl5.pu()
mbl5.color('white')
mbl5.shape('circle')
mbl5.turtlesize(1.5)
mbl5.left(180)

mbl6 = Turtle()
mbl6.shape('circle')
mbl6.color('red3')
mbl6.pu()
mbl6.color('white')
mbl6.shape('circle')
mbl6.turtlesize(1.5)

mbl7 = Turtle()
mbl7.shape('circle')
mbl7.color('red3')
mbl7.pu()
mbl7.color('white')
mbl7.shape('circle')
mbl7.turtlesize(1.5)
mbl7.left(180)

mbl8 = Turtle()
mbl8.shape('circle')
mbl8.color('red3')
mbl8.pu()
mbl8.color('white')
mbl8.shape('circle')
mbl8.turtlesize(1.5)

import time
def move(marble1,marble2,marble3,marble4,marble5,marble6,marble7,marble8) :
    t1=50
    t2=0
    t3=25
    t4=75
    t5=37.5
    t6=62.5
    t7=12.5
    t8=87.5
    
    
    
    while True:
        t1=t1+1
        t2=t2+1
        t3=t3+1
        t4=t4+1
        t5=t5+1
        t6=t6+1
        t7=t7+1
        t8=t8+1
        turtle.tracer(0)
        mbl1.setx(250*sin(t1*pi/100))
        mbl2.sety(250*sin(t2*pi/100))
        mbl3.setx(cos(pi/4)*250*sin(t3*pi/100))
        mbl3.sety(sin(pi/4)*250*sin(t3*pi/100))
        mbl4.setx(cos(pi/4)*250*sin(t4*pi/100))
        mbl4.sety(-sin(pi/4)*250*sin(t4*pi/100))
        mbl5.setx(cos(pi/8)*250*sin(t5*pi/100))
        mbl5.sety(sin(pi/8)*250*sin(t5*pi/100))
        mbl6.setx(cos(pi/8)*250*sin(t6*pi/100))
        mbl6.sety(-sin(pi/8)*250*sin(t6*pi/100))
        mbl7.setx(cos(3*pi/8)*250*sin(t7*pi/100))
        mbl7.sety(sin(3*pi/8)*250*sin(t7*pi/100))
        mbl8.setx(cos(3*pi/8)*250*sin(t8*pi/100))
        mbl8.sety(-sin(3*pi/8)*250*sin(t8*pi/100))
        time.sleep(0.015)
        turtle.update()
        

move(mbl1,mbl2,mbl3,mbl4,mbl5,mbl6,mbl7,mbl8)


