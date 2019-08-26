import turtle   # 리컨시브 콜  순환함수

def tree(length):
    if length > 5:            # length가 5보다 크면 순환
        t.forward(length)  # 거북이가 length 만큼 직
        t.right(20)                # 오른쪽으로 20도 회전
        tree(length-15)      # (length-15) 를 인수로 tree()를 순환
        t.left(40)               # 왼쪽으로 40도 회전
        tree(length-15)     # (length-15) 를 인수로  tree()를 순환
        t.right(20)                 # 오른쪽으로 20도 회전
        t.backward(length)    #length만큼 뒤로 간다.

t = turtle.Turtle()     # 거북이가 위쪽을 향하게 
t.left(90)

t.color("green")   # 선의 색 : 녹색
t.speed(1)     # 속도를 제일 느리께
tree(90)     #길이 90으로 tree() 호

        
    
