import turtle as t

#n=100
n=int(t.textinput("","반복횟수? : "))
sp=int(t.textinput("", "Speed? : "))

t.bgcolor("black")  # 백그라운드 색
t.color("green")  # 선색

#t.speed(0)  # 가장 빠른 거북이 속도 // 숫자가 작을수록 느린속
t.speed(sp)
             
for x in range(n):
    t.circle(80)
    t.lt(360/n)
        
    
