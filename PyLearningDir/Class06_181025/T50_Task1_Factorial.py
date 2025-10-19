# Given a Number you need to calculate the factorial of that number

number = int(input("Enter a number: ").strip())
f = 1
for i in range(number,0,-1):
    f = f * i
    print("Factorial Number: ",f)

# import math
# f1=math.factorial(number)
# print(f1)






