l = int(input('Enter lower limit'))
h = int(input('Enter higher Limit'))
print(f'all Prime numbers between {l} and {h} are' )
for a in range(l,h+1):
    c = 0
    for b in range(1,a+1):
        if a%b == 0:
            c += 1
    if c==2:
        print(a, end = '  ')
