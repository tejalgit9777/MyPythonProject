

# n= int(input("Enter a number: "))
# j=0
# for i in range(n,0,-1):
#     for j in range(1,i):
#         print(j,end=" ")
#     print(" ")
#
# n1= int(input("Enter a number: "))
# j1=0
# for i1 in range(n1+1):
#     for j1 in range(1,i1):
#         print(j1,end=" ")
#     print(" ")

# n2= int(input("Enter a number: "))
# j2=0
# for i2 in range(n2+1):
#     for j2 in range(n2-i2):
#         print(" ", end=" ")
#     for k in range(i2):
#         print("*", end=" ")
#     print(" ")

# n3= int(input("Enter a number: "))
# j3=0
# for i3 in range(n3,0,-1):
#     for j3 in range(n3-i3):
#         print(" ", end=" ")
#     for k2 in range(i3):
#         print("*", end=" ")
#     print(" ")

n = 7  # Must be an odd number for a symmetric diamond
mid = n // 2  # Middle index

for i in range(n):
    for j in range(n):
        if abs(i - mid) + abs(j - mid) == mid:
            print("*", end="")
        else:
            print(" ", end="")
    print()
