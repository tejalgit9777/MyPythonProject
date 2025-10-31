# Print value of square and number input by user

def square(n):
    if n<0:
        print("The number is negative")
    elif n>0:
        print("Square Number: ",n*n)

n=int(input("Enter a number for square: ").strip())
square(n)