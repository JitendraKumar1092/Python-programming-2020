# Python program to find armstrong numbers in given range
# Input section
l = int(input("Enter the lower range - "))
h = int(input("Enter the higher range - "))
#Logic section and output section
for num in range(l,h+1):
    total = 0
    a = len(str(num))
    copy = num
    while num != 0:
        d = num % 10
        total += (d**a)
        num = num//10
    if copy == total:
        print(copy ,end = ' ,')

