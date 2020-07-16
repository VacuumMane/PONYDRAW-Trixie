import turtle as t
from math import *

def flyto(x,y): #抬笔到某个点
    t.penup()
    t.goto(x,y)
    t.pendown()

def flyfd(angle,distance): #从所在点抬笔向某方向移动一段距离
    t.penup()
    t.seth(angle)
    t.fd(distance)
    t.pendown()

def eclipse(x,y,a,b,angle1,angle2,angle3): #原点，半径，起画相对角度，斜度，弧度
    step=360 #分割份数
    per=angle3/step
    x1=a*cos(radians(angle1))
    y1=b*sin(radians(angle1))
    flyto(x+x1*cos(radians(angle2))-y1*sin(radians(angle2)),y+x1*sin(radians(angle2))+y1*cos(radians(angle2)))
    for i in range(1,step+1):
        x1=a*cos(radians(angle1+i*per))
        y1=b*sin(radians(angle1+i*per))
        t.goto(x+x1*cos(radians(angle2))-y1*sin(radians(angle2)),y+x1*sin(radians(angle2))+y1*cos(radians(angle2)))

def color(color1,color2): #具体color格式需设置
    t.pencolor(color1)
    t.fillcolor(color2)

def filleclipse(x,y,a,b,angle1,angle2,angle3): #上色的椭圆
    t.begin_fill()
    eclipse(x,y,a,b,angle1,angle2,angle3)
    t.end_fill()

def drawEye(x0,y0): #椭圆圆心 眼瞳内及眉毛方向

    step=360 #分割份数
    angle=360/step

    #眼白
    t.pensize(1)
    color((217,245,239),(255,255,255))
    a=30
    b=60 #半径
    filleclipse(x0,y0,a,b,0,0,360)

    #outer眼瞳(左方位置错误)
    t.pensize(1)
    color((99,71,115),(107,78,122))
    c=20
    d=40 #半径
    x1=x0-a+c
    y1=y0
    filleclipse(x1,y1,c,d,0,0,360)

    #innner眼瞳
    t.pensize(1)
    color((0,0,0),(0,0,0))
    e=10
    f=20 #半径
    x2=x0-a+e
    y2=y0
    filleclipse(x2,y2,e,f,0,0,360) 

    #反光
    t.pensize(1)
    color((255,255,255),(255,255,255))
    g=5
    h=10 #半径
    x3=x0-a+g
    y3=y0
    filleclipse(x3,y3,g,h,0,0,360) 

    #眉毛 可以模拟渐变
    t.pensize(5)
    color((0,0,0),(0,0,0))
    i=30
    j=60 #半径
    x4=x0
    y4=y0
    eclipse(x0,y0,a,b,20,0,170)
    def eyebrow(i,j,x4,y4,radian,bia): #眉毛尖
        t.pensize(3)
        t.pencolor(0,0,0)
        for i in range(3): #数量
           eclipse(x0,y0,a,b,20+i*20,0,20) #沿着眼眶...间隔
           t.seth(bia+i*20) #尖初始方向
           t.circle(50,radian) #曲度
           t.circle(50,-radian)
    eyebrow(i,j,x4,y4,30,15)

def drawNose():
    t.colormode(255)
    t.pencolor(62,151,202)
    t.pensize(5)
    size=20
    x1=0
    y1=0 #与drawFace中相同
    flyto(x1,y1)
    flyfd(-90,size*3/4)
    t.seth(0)
    t.circle(-size*3,15)
    t.circle(-size*3,-30)
    t.circle(-size*3,15)#the upper part
    flyfd(-25,size)
    t.right(90)
    t.circle(-20,size*3/4)
    t.left(90) #the left of the lower part
    t.penup()
    t.bk(20)
    t.pendown() #back to the start
    flyfd(205,size)
    t.left(90)
    t.circle(-20,size*3/4)
    t.right(90) #the right of the lower part
    t.penup()
    t.bk(size)
    t.pendown()

def drawMouth():
    t.colormode(255)
    t.pencolor(62,151,202)
    t.pensize(5)
    size=20 #与drawNose中相同
    flyfd(-90,size*2)
    t.seth(0)
    t.circle(-size*3,15)
    t.circle(-size*3,-15*2)
    t.circle(-size*3,15)

def drawUnicorn():

    length=100 #斜边长
    width=25 #弧度
    flyto(0,90) #与face大小有关
    t.seth(0)
    t.penup()
    t.circle(length,width/2)
    t.pendown()

    t.left(90)
    t.pensize(8)
    color((60,149,201),(116,183,231))
    t.begin_fill()
    t.seth(90+width/2)
    t.fd(length)
    t.seth(270-width/2)
    t.fd(length)
    t.seth(-width/2)
    t.circle(length,width/3)
    t.end_fill()
    t.penup()
    t.circle(length,width*(1-1/3))
    t.pendown()

    t.pensize(3)
    for i in range(3): #角纹数
        flyfd(90+width/2,length/4)
        t.seth(180+width/2)
        t.circle(-length*(4-(i+1))/4,width)
        t.penup()
        t.circle(-length*(4-(i+1))/4,-width)
        t.pendown()

def drawEar(): #一只耳

    flyto(120,0)
    t.seth(90)
    t.penup()
    t.circle(120,5)
    t.pendown()

    #耳廓
    t.pensize(8)
    color((60,149,201),(116,183,231))
    t.begin_fill()
    t.seth(45)
    t.circle(120,90)
    t.pensize(7)
    t.circle(15,105)
    t.pensize(8)
    t.circle(160,30)
    t.end_fill()

    #“中线”
    flyto(120,0)
    t.seth(90)
    t.penup()
    t.circle(120,25)
    t.pendown()
    t.seth(60)
    for i in range(7): #模拟粗细渐变
        t.pensize(i+1)
        t.circle(120,25/7)
    for i in range(7):
        t.pensize(6-i)
        t.circle(120,25/7)

def drawDWHair(): #单色版本

    t.pensize(10)
    color((153,211,241),(218,240,251))
    flyto(0,10)
    t.begin_fill()
    t.seth(0)
    t.fd(100)
    t.seth(-60)
    t.circle(-120,60)
    t.circle(12,200)
    t.seth(-90)
    t.circle(-28,180)
    t.circle(-120,30)
    t.end_fill()

def drawUPHair():

    t.pensize(10)
    color((153,211,241),(218,240,251))
    t.begin_fill()

    eclipse(0,0,220,120,90,-60,160)
    x=0
    y=0
    a=220
    b=120
    angle1=90
    angle2=-60
    angle3=160

    t.seth(280)
    t.circle(-15,180)
    t.circle(-120,15)
    t.seth(230)
    t.circle(48,90)
    t.circle(30,120)
    t.circle(48,15)
    t.circle(-121,50)
    t.circle(-50,90)
    t.left(100)
    t.circle(-50,90)
    x1=a*cos(radians(angle1))
    y1=b*sin(radians(angle1))
    t.goto(x+x1*cos(radians(angle2))-y1*sin(radians(angle2)),y+x1*sin(radians(angle2))+y1*cos(radians(angle2)))
    t.end_fill()


def drawFace():

    t.colormode(255)
    drawDWHair()

    #脸型
    t.pensize(10)
    color((60,149,201),(116,183,231))
    r=120 #半径
    x1=0
    y1=0 #圆心
    flyto(x1+r,y1) 
    t.seth(90) #就先不管歪头的情况了
    t.begin_fill()
    t.circle(r,360)
    t.end_fill()

    drawNose()
    drawMouth()
    drawEye(r*cos(radians(180-14))*4/7,r*sin(radians(180-14))*4/7) #右眼
    drawUPHair()
    drawEar()
    drawEye(r*cos(radians(14))*4/7,r*sin(radians(14))*4/7) #左眼
    drawUnicorn()

#t.tracer(False)
drawFace()
t.done()