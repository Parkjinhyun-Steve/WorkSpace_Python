inFp, outFp = None, None
inStr = ''

inFp = open('c:/windows/notepad.exe','rb')
outFp = open('c:/temp/notepad.exe','wb')

while True:
    inStr=inFp.read(1)
    if not inStr:
        break
    outFp.write(inStr)

inFp.close()
outFp.close()
print('---이진 파일이 정상적으로 복사되었음---')
