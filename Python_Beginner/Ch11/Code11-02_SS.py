inFp = None
nStr = ''

inFp = open('C:/temp/data1.txt', 'r', encoding='UTF8')

while True:
    for i, line in enumerate(inFp):
        inStr = inFp.readline()
        if inStr == '':
            
        print(inStr, end='')
    break;

inFp.close()
        