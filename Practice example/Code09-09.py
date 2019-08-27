def multi(v1, v2):
    reList=[]
    res1 = v1 + v2
    res2 = v1 - v2
    reList.append(res1)
    reList.append(res2)
    return reList

myList =[]
sum, sub = 0,0

myList = multi(100,200)
sum = myList[0]
sub = myList[1]

print("multi()에서 돌려준 값 ==> %d, %d\n" %(sum, sub))

print(myList)
