# input section
num = int(input("Enter a number to find it's factors - "))
#logic section
ls = []
for i in range(1,num+1):
    if num % i == 0:
        ls.append(i)
#output section
print(ls)