def count(num):
    if num >= 1:
        print(num, end = ' ')
        count(num - 1)
    else :
        return
    

count(20)