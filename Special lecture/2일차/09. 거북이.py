import turtle as t

t.width(3)   # 선의 두께 3

t.shape("turtle")

t.shapesize(3, 3)  # 거북이 3배 확

# 무한 루프

while True :
    key=input("키보드 L : left, R : Right 입력하기 ")
    if key == "L" :       # L 을 입력
        t.left(90)             # lt 로 사용 가능
        t.forward(100)    # fd 사용 가능
    if key == "R" :      # R 을 입력
        t.right(90)           # rt로 사용 가
        t.forward(100)
    
