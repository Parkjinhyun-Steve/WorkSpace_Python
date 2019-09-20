inFp = None
inList, inStr = [], ''

inFp = open('c:/temp/data1.txt','r',encoding='UTF8')

inList = inFp.readlines()
for inStr in inList:
    print(inStr, end='')

inFp.close()