import turtle as t
from math import *

def flyto(x,y,a,b): #抬笔到某个点（画椭圆适应版）
    t.penup()
    t.goto(x+a,y)
    t.pendown()

def flyfd(angle,distance): #从所在点抬笔向某方向移动一段距离
    t.penup()
    t.seth(angle)
    t.fd(distance)
    t.pendown()

def eclipse(x,y,a,b,angle): #填色版
    step=360 #分割份数
    per=angle/step
    flyto(x,y,a,b) 
    #t.seth(0+90) 椭圆斜度(暂时废弃)
    t.begin_fill()
    for i in range(1,step+1):
        t.goto(x+a*cos(radians(i*per)),y+b*sin(radians(i*per))) #不加radians不行，但是很好看
    t.end_fill()

def drawFace(): #还差头发 角 耳朵
    t.colormode(255)
    t.pencolor(60,149,201)
    t.pensize(10)
    t.fillcolor(116,183,231)
    r=120 #半径
    x1=0
    y1=0 #圆心
    flyto(x1,y1,r,0) 
    t.seth(90) #就先不管歪头的情况了
    t.begin_fill()
    t.circle(r,360)
    t.end_fill()
    drawNose()
    drawMouth()
    drawEye(r*cos(radians(14))*4/7,r*sin(radians(14))*4/7)
    drawEye(r*cos(radians(180-14))*4/7,r*sin(radians(180-14))*4/7)

def drawEye(x0,y0): #椭圆圆心 还差眉毛
    t.colormode(255)
    t.pencolor(217,245,239)
    t.pensize(1)
    t.fillcolor(255,255,255)
    step=360 #分割份数
    angle=360/step
    #眼白
    a=30
    b=60 #半径
    eclipse(x0,y0,a,b,360)
    #outer眼瞳(左方位置错误)
    t.pencolor(99,71,115)
    t.pensize(1)
    t.fillcolor(107,78,122)
    c=20
    d=40 #半径
    x1=x0-a+c
    y1=y0
    eclipse(x1,y1,c,d,360)
    #innner眼瞳
    t.pencolor(0,0,0)
    t.pensize(1)
    t.fillcolor(0,0,0)
    e=10
    f=20 #半径
    x2=x0-a+e
    y2=y0
    eclipse(x2,y2,e,f,360) 
    #反光
    t.pencolor(255,255,255)
    t.pensize(1)
    t.fillcolor(255,255,255)
    g=5
    h=10 #半径
    x3=x0-a+g
    y3=y0
    eclipse(x3,y3,g,h,360) 
    #眉毛
    t.pencolor(0,0,0)
    t.pensize(5)
    t.fillcolor(0,0,0)
    i=30
    j=60 #半径
    x4=x0
    y4=y0
    step=360 #分割份数
    per=180/step
    flyto(x4+i*cos(radians(60))-i,y4+j*sin(radians(60)),i,j) 
    t.seth(0+150) #椭圆斜度(暂时废弃)
    for i in range(1,step+1):
        t.goto(x4+i*cos(radians(i*per+60)),y4+j*sin(radians(i*per+60))) #不加radians不行，但是很好看
    #eclipse(x4,y4,i,j,360)

def drawNose():
    t.colormode(255)
    t.pencolor(62,151,202)
    t.pensize(5)
    size=20
    x1=0
    y1=0 #与drawFace中相同
    flyto(x1,y1,0,0)
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

#t.tracer(False)
drawFace()
t.done()