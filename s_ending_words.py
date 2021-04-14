#python program to print all words ending with 's'
st = input('enter your words')
st = st.split()
for i in st:
    a = i.endswith('s')
    if a:
        print(i)
