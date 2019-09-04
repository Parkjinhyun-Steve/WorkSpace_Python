aa = []
for i in range(0,10):
    aa.append(0)

sum = 0

for i in range(0,10):
    aa[i]=int(input(str(i+1) + "번째 숫자 : "))

sum = aa[0] + aa[1] + aa[2] + aa[3]+ aa[4]+ aa[5]+ aa[6] + aa[7] + aa[8] + aa[9]

print("합계 ==> %d" % sum)


i = 0
sum = 0

while i < 10:
    sum = sum + aa[i]
    i = i + 1
    

print("합계 ==> %d" % sum)