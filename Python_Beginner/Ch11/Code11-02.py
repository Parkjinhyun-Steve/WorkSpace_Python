inFp = None
nStr = ''

inFp = open('C:/temp/data1.txt', 'r', encoding='UTF8')

while True:
    inStr = inFp.readline()
    if inStr == '':
        break;
    print(inStr, end='')

inFp.close()
        
