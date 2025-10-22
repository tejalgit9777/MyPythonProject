#Count digits in a number

n= int(input("Enter a number: ").strip())

counter = 0
if n==0:
    count = 1
while n > 0:
    counter = counter + 1
    n = n // 10
print(counter)

