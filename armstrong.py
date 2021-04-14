num = int(input())
copy = num
sum = 0
a = len(str(num))
while num != 0:
    d = num % 10
    sum += (d**a)
    num = num//10
if copy == sum:
    print(copy,"is a armstrong number")
else:
    print(copy,' is not an armstron number')
