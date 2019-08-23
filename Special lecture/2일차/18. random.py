import random
n = random.randint(1,30)  # 1~30까지 랜덤 수를 n에 저장

while True:
    n1=input("숫자를 입력하시오")
    g=int(n1)
    if g == n:
        print("정답!!")
        break
    if g < n:
        print("작아요")
    if g > n:
        print("커요")
    

