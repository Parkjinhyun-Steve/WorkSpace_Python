import random

a=random.randint(1, 30)
b=random.randint(1, 30)


print(a, "+", b,"=")
x=input()   # 입력받은 값을 변수 x에 저장한다.
c=int(x)   # 변수 x타입을 int형으로 변경한다.

if a+b==c:
    print("천재")
else:
    print("바보")
