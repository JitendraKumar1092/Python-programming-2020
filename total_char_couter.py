st = input('enter the string - ')
lst = []
for i in st:
    if i not in lst:
        print(i,'=',st.count(i))
        lst.append(i)