import random
import turtle

def draw_maze(x,y):
    for i in range(2):
        t.penup()
        if i==1:
            t.goto(x+100, y+100)
        else:
            t.goto(x,y)
        t.pendown()
        t.forward(300)
        t.right(90)
        t.forward(300)
        t.left(90)
        t.forward(300)
        
def turn_left():  # 거북이가 왼쪽으로 10도 10칸 가는 함수
    t.left(10)
    t.forward(10)

def turn_right():  # 거북이가 오른쪽으로 10도 10칸 가는 함
    t.right(10)
    t.forward(10)

t = turtle.Turtle()    # import turtle as t  <- 이걸로 대신 써도 된다.
screen = turtle.Screen()

t.shape("turtle")
t.speed(0)

draw_maze(-300, 200)   # -300 부터 200 까지  그린다.  (0,0은 화면 중앙)
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

t.penup()     
t.goto(-300, 250)
t.speed(1)
t.pendown()

screen.listen()    # 스크린 제어 함수
screen.mainloop()   # x,y 좌표를 계속 반복 진행할 수 있도록 한다.






