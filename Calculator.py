def add(x, y):
    return x + y
def subt(x, y):
    return x - y
def mult(x, y):
    return x * y
def divide(x, y):
    return x / y
num1 = int(input("Enter the first num - "))
choice = input("Enter the operation (+,-,*,/ ")
num2 = int(input("Enter the second number"))

if choice == '+':
    print(f"addition of {num1} and {num2} is,",add(num1,num2))
if choice == '-':
    print(f"subtraction  of {num1} and {num2} is,",subt(num1,num2))
if choice == '*':
    print(f"multiplication of {num1} and {num2} is,",mult(num1,num2))
if choice == '/':
    print(f"division of {num1} and {num2} is,",divide(num1,num2))