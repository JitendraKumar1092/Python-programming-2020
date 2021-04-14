st = input('enter string')
lst = []
for i in st:
    if i not in lst :
        print(i, end='',sep='')
        lst.append(i)
