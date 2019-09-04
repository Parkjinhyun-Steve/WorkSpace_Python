import time

input ("엔터키를 누르고 20초를 세어보세요")

start = time.time()

input("20초 후에 엔터키를 누르시오")

end = time.time()

et = end - start
print("실제시간 =", et, "초")
print("차이시간 =", abs(et-20), "초")
