# Remove all Characters in a String except alphabet
st = input()
new_st = str()
for char in st:
    if char <= 'z' and char >= 'a':
       new_st += new_st.join(char)
    elif char >= 'A' and char <= 'Z' :
        new_st += new_st.join(char)
print(new_st)

