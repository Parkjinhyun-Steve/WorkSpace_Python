def square(a):  # 사각형 면적 구하기 
    c=a*a
    return c

def triangle(a, h): # 삼각형 면적 구하기 
    c=a * (h/2)
    return c

s1 = 4
s2 =square(s1) 
print(s1, s2)

print(triangle(3, 5))  # 인자(파라메터) 갯수가 맞아야 한다.

