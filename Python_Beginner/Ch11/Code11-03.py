inFp = None
inList = ''

inFp = open('c:/temp/data1.txt','r',encoding='UTF8')

inList = inFp.readlines()
print(inList)

inFp.close()