# pattern
#               *
#               * *
#               * * *

n= int(input("Enter a number: ").strip())
i,j=0,0
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()



