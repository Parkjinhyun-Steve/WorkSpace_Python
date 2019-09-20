inFp = None
inList = ''

with open('c:/temp/data1.txt','r',encoding='UTF8') as inFp:
    inList = inFp.readlines()
    print(inList)