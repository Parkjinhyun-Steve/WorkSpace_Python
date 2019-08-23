import random  # 프로젝트1 : 계산 문제를 맞추는 사람

def make_question():
    a = random.randint(1, 40)  # 1-40 사이의 임의 수를 a에 저장
    b = random.randint(1, 20)  # 1-20 사이의 임의 수를 b에 저장
    op = random.randint(1, 3) # 1-3 사이의 임의 수를 op에 저

    q = str(a)  #  정수 a를 문자열로 바꾸어 q에 저장 -> q에 문제 생성

    if op == 1:   # 연산자 추가 / op 값이 1이면 덧셈 문제 생성
        q = q+ "+"
    if op == 2:   # 연산자 추가 / op값이 2면 뺄셈 문제 생성
        q = q+ "-"
    if op ==3:   # 연산자 추가 / op값이 3이면 곱셈 문제 생
        q = q+ "*"

    q = q + str(b)  # 

    return q  # 만들어진 문제 리

sc1 = 0   # 정답 횟수 저장 변수
sc2 = 0  #  오답 횟수 저장 변수

for x in range(5):  # 5문제 생성
    q = make_question()  
    print(q)  # 문제 출력
    ans = input("=")    # 사용자 정답 입력
    r = int(ans)  # 정답 타입을 정수로 변

    if eval(q) == r:   #문제 q를 컴퓨터가 계산한 결과인 eval(q)와 비교하여 정답 및 오답 판
        print("정답!")
        sc1 = sc1 + 1
    else:
        print("오답!")
        sc2 = sc2 + 1

print("정답", sc1, " 오답", sc2)
if sc2 == 0:    
    print("당신은 천재입니다!")  # 오답이 0일때 출력
        
