# 1~10 까지 홀수(odd) 의 합 (sum)
sum=0
for x in range(1,10,2): # 1:처음값   11:끝 값(최종)   2:증가
    sum=sum+x
    print("x=", x ,"sum=", sum)



# 1~10 까지 짝수(even)의 합 (sum)
sum=0
for x in range(2,1100000000,2): # 0:처음값  10:끝 값(최종)   2:증가
    sum=sum+x
    print("x=", x ,"sum=", sum)

