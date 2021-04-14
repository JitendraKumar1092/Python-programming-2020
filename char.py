a = input()
if (a<='Z' and a>='A'):
    print('uppercase')
elif (a <= 'z' and a >= 'a' ):
    print('lower case')
elif (
    a >= '0' and a<='9' ) :
    print('it is a digit')
else :
    print('special character')
