#input section
num1 = int(input("Enter first number - "))
num2 = int(input("Enter second number - "))
num3 = int(input("Enter third number - "))
#logic section
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
#output section
print(f"Largest number among {num1}, {num2}, {num3} is {largest}")