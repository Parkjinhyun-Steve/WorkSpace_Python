import turtle    # 터틀 그래필 모듈을 불러온다.
import random   # 난수 모듈을 불러온다.

screen= turtle.Screen()
image1 = "rabbit.gif"
image2 = "turtle.gif"

screen.addshape(image1)
screen.addshape(image2)

t1 = turtle.Turtle()   #첫번재 거북이를 생성한다.
t1.shape(image1)
t1.pensize(5)   # 펜의 두께
t1.penup()     #펜을 든다
t1.goto(-300,0)    # 시작 위치로 간다

t2 = turtle.Turtle()   # 두번째 거북이를 생성한다
t2.shape(image2)
t2.pensize(5)   
t2.penup()
t2.goto(-300,-200)

t1.pendown()   # 첫번째 거북이의 펜을 내린다
t2.pendown()    # 첫번째 거북이의 펜을 내린다
t1.speed(1)
t2.speed(1)

for i in range(40):   # 100번 반복한다
    d1=random.randint(1, 30)  # 1부터 60 사이의 난수를 발생한다.
    t1.forward(d1)    # 난수만큼 이동한다
    d2=random.randint(1,30)  
    t2.forward(d2)




