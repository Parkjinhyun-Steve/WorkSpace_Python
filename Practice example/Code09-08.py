def func1():
    result = 100
    return result

def func2():
    print("반환값이 없는 함수 실행")


sum = 0

sum = func1()
print("func1()에서 돌려준 값 ==> %d" %sum)
func2()