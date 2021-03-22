text = input()
lenth= len(text)
stir = text.lower()
vc=0
cc=0
sc=0
for i in range (lenth):
    if stir[i] in ('a','e','i','o','u'):
        vc= vc + 1 
    elif stir[i] >= 'a' and stir[i] <= 'z' :
        cc = cc + 1 
    else:
        sc =  sc +1 
print('vowels = ',vc, 'consonant = ',cc,'special characters =',sc)

