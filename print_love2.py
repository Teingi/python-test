from turtle import *
from time import sleep

def go_to(x, y):
   up()
   goto(x, y)
   down()


def big_Circle(size):  #函数用于绘制心的大圆
   speed(100)
   for i in range(150):
       forward(size)
       right(0.3)

def small_Circle(size):  #函数用于绘制心的小圆
   speed(100)
   for i in range(210):
       forward(size)
       right(0.786)

def line(size):
   speed(10)
   forward(51*size)

def heart( x, y, size):
   go_to(x, y)
   left(150)
   begin_fill()
   line(size)
   big_Circle(size)
   small_Circle(size)
   left(120)
   small_Circle(size)
   big_Circle(size)
   line(size)
   end_fill()

def arrow():
   pensize(10)
   setheading(0)
   go_to(-400, 0)
   left(15)
   forward(150)
   go_to(339, 178)
   forward(150)

def arrowHead():
   pensize(1)
   speed(50)
   color('red', 'red')
   begin_fill()
   left(120)
   forward(20)
   right(150)
   forward(35)
   right(120)
   forward(35)
   right(150)
   forward(20)
   end_fill()


def main():
   pensize(2)
   color('red', 'pink')
   #getscreen().tracer(30, 0) #取消注释后，快速显示图案
   heart(200, 0, 1)          #画出第一颗心，前面两个参数控制心的位置，函数最后一个参数可控制心的大小
   setheading(0)             #使画笔的方向朝向x轴正方向
   heart(-80, -100, 1.5)     #画出第二颗心
   arrow()                   #画出穿过两颗心的直线
   arrowHead()               #画出箭的箭头
   go_to(400, -300)
   write("To小仙女——By臭猪", move=True, align="right", font=("宋体", 30, "normal"))
   done()

main()
