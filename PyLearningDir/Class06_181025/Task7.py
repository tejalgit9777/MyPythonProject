#. Multiplication table

# number = int(input("Enter a number: ").strip())
# j = 1
# if number < 0:
#     print("Enter a positive number")
# else:
#     for j in range(1, number+1):
#         j = print(number,"*",j,"=",j * number)


#While

n2 = int(input("Enter a number: ").strip())
k = 1
if n2 < 0:
    print("Enter a positive number")
else:
    while k <= n2:
        print(n2,"*",k,"=",k * n2)
        k +=1


