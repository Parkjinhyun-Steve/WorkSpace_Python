import turtle as t

n=100
t.bgcolor("black")  # 백그라운드 색
t.color("green")  # 선색
t.speed(0)  # 가장 빠른 거북이 속도 // 숫자가 작을수록 빠른속

for x in range(n):
    t.circle(80)
    t.lt(360/n)
        
    
