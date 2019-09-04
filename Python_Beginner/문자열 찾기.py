ss='파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠. ^^'
ss.count('공부')

print(ss.find('공부'), ss.rfind('공부'), ss.find('공부',21), ss.find('없다'))
print(ss.index('공부'), ss.rindex('공부'), ss.index('공부',21))
print(ss.startswith('파이썬'), ss.startswith('파이썬',0), ss.endswith('^^'))