lst = input('enter items').split()
re = list(map(len, lst))
re.sort()
print(re)