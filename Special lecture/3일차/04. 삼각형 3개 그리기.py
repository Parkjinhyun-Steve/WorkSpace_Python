
import turtle as t

t.shape("turtle")

def square(length):   # 한 변ㄱ의 길이
    for i in range(3):
        t.forward(length)
        t.left(360/3)

t.up()
t.goto(-200,0)
t.down()
square(100);

t.up()
t.goto(0 ,0)
t.down()
square(100);

t.up()
t.goto(200 ,0)
t.down()
square(100);



        
