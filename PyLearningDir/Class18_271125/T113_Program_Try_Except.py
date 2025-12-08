
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Division by zero error b!=0")
