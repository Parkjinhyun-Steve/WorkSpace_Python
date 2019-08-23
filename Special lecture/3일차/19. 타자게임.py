# 프로젝트 2 : 타자게임 만들기
import random
import time

w= ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]  # 단어 리스트
n=1   # 문제 번호

print("[타자게임] 준비되면 엔터!")
input()  # 사용자 엔터 입력

start = time.time()  # 시작 시간 기록

q = random.choice(w) #단어 리스트에서 랜덤 선택
while n <=5:  # 문제 5회 반복
    print("*문제", n)
    print(q)  # 문제 출력
    x = input()  # 사용자 정답 입력
    if q == x:  # 같을때 
        print("통과!")  # 통과! 출력 
        n = n+1 # 문제 번호 1 증가
        q = random.choice(w) # 새 문제 랜덤 선택
    else:
        print("오타! 다시도전!")

end = time.time()  # 끝 시간 기록
et = end - start # 시간 계산 
et = format(et, ".2f") # 소수점 2자리 표기
print("타자시간: ", et, "초")

       

