import turtle as t

t.shape("turtle")
t.color("red", "yellow")
t.begin_fill()

while True:
    t.backward(200)
    t.left(170)
    if abs(t.position()) < 1:   # positiont()dml 약자 : pos() 현재 좌표를 (x,y)에 저장한다.
        break
t.end_fill()



