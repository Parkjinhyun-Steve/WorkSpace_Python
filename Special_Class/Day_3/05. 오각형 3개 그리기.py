
import turtle as t

t.shape("turtle")

def pentagon(length):   # 한 변의 길이
    for i in range(5):
        t.forward(length)
        t.left(360/5)

t.up()
t.goto(-200,0)
t.down()
pentagon(100);

t.up()
t.goto(0 ,0)
t.down()
pentagon(100);

t.up()
t.goto(200 ,0)
t.down()
pentagon(100);



        
