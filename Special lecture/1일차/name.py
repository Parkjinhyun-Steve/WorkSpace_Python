import turtle as t

t.shape("turtle")
s = t.textinput("Input your name!!", "이름을 입력하세요.")
t.write("      안녕하세요?  " + s + "씨, 터틀 인사드립니다.")

t.color("red")
t.pensize(2)

for x in range(3) :
    t.left(120)
    t.forward(100)

t.color("yellow")
t.pensize(3)

for x in range(4) :
    t.left(90)
    t.forward(100)

t.color("green")
t.pensize(4)

for x in range(5) :
    t.left(72)
    t.forward(100)

t.color("blue")
t.pensize(5)

for x in range(6) :
    t.left(60)
    t.forward(100)
