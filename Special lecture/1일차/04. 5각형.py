# 5각형 & for

import turtle as t
t.shape("turtle")

t.color("blue")
t.pensize(3)

for x in range(5) :
    t.left(72)
    t.forward(120)


# 5각형 & for & n & fill

t.color("red")
t.pensize(4)
t.forward(50)

n=5
t.begin_fill()

for x in range(n) :
    t.left(360/n)
    t.forward(120)

t.end_fill()


# 5각형 & for & n & fill & input

n = int(t.textinput ("", "몇각형 입니까?"))  #""(널)Null

t.color("green")
t.pensize(4)
t.forward(50)

    # t.begin_fill()

for x in range(n) :
    t.left(360/n)
    t.forward(120)

    # t.end_fill()
