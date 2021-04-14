st = input('enter the main string - ')
rem_st = input('enter the string whose characters you want to remove from main string - ')
re = ''
for i in st:
    if i not in rem_st:
        re += i
print('after removal your resulting string is',re)
