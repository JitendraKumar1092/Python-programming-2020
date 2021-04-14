num= int(input("enter the number "))
i=2
c = True
while i < num:
    if num % i == 0:
        c = False
    i += 1
if(c):
    print("given number is prime")
else :
    print("not a prime number")
