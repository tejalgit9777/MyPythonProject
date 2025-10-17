#Find Number id odd or even

n= int(input("Enter Number: "))
# if n > 0:
#     if n % 2 == 0:
#         print(n, "is even")
#     else:
#         print(n, "is odd")
# else:
#     print(n, "is negative")

if n>0:
    print("is even" if (n % 2) == 0 else "is odd")
else:
    print("is negative")