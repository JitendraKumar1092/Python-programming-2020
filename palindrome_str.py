st = input('enter a string - ')
copy = st[::-1]
if st == copy:
    print(f"given string {st} is palindrome")
else:
    print(f"given string '{st}'is not palindrome")
