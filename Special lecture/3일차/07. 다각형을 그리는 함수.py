import turtle as t

def polygon(n):       #인수가 1개 
     for x in range(n):
         t.forward(50)
         t.left(360/n)    #거북이를 360/n 만큼 왼쪽으로 회전

def polygon2(n, a):  #인수가 2개
    for x in range (n):
        t.forward(a)
        t.left(360/n)  #거북이를 360/n 만큼 왼쪽으로 회전

polygon(3)   # 삼각형
polygon(5)   # 오각형

t.up()
t.forward(100)
t.down()

polygon2(5, 75)  # 오각형, 길이 75
polygon2(4, 100)  # 사각형, 길이 100

