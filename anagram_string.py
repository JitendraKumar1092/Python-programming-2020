#input section
st1 = input('enter the first string - ')
st2 = input('enter the second string - ')
#logic section
sort1 = set(sorted(st1))
sort2 = set(sorted(st2))

if sort2 == sort1:
    print("given string is anagram")
else:
    print("not an anagram string")