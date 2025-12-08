
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
try:
    c = a / b
    print(c)
except (ZeroDivisionError, TypeError, ValueError, IndexError, NameError):
    print("Error Due to the Type, Name, Value, Index or Zero Div!")
