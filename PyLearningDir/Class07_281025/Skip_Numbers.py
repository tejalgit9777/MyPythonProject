# Skip numbers divisible by 3, from (0,100)
from email.headerregistry import UniqueSingleAddressHeader

#n= int(input("Enter a number: ").strip())

for i in range(1,101):
    if i % 3 == 0:
        continue
    print(i,end=' ')
print()

# Using While loop

j=0
while j<101:
    if j % 3 == 0:
        j+=1
        continue
    print(j,end=' ')
    j+=1




