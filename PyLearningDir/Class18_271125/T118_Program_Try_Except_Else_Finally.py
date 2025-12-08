
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
try:
    c = a / b
    d = a + b
except ZeroDivisionError:
    print("Error Due to the division by Zero Div b!=0")
except ValueError:
    print("Value Error")
else:
    print(c)  # Runs only if try block succeeds.
    print(d)
finally:
    print("Executed!!")
