
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Error Due to the division by Zero Div b!=0")
except ValueError:
    print("Value Error")
finally:
    print("Executed!!")
