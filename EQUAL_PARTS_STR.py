str = input('enter string')
length = len(str)

n = int(input("enter no. of parts"))
j = 0
char = length//n

out = []

if(length % n != 0):
        print("Sorry this string cannot be divide into equsl parts")
else:
    for i in range(0, length, char):

        k = str[ i : i+char]
        out.append(k)
    print("Equal parts of given string ")
    for i in out:
        print(i,end = ', ')