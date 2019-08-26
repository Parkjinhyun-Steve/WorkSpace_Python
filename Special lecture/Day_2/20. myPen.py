import turtle as myPen

myPen.speed(1)
myPen.color("#ff0000")

for y in range(1,37):
    for x in range(1,6):
        myPen.left(144)  # 그량죠 별 각도 : 144도!
        myPen.forward(200)
        print("x:",x)
    print("y:",y)
    myPen.left(10)
