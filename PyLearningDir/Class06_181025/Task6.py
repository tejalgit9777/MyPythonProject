#Sum of first N natural numbers

n = int(input("Enter Number: ").strip())
s=0
for i in range(1,n,1):
    s = s + i
print("sum: ",s)

# while loop

n1 = int(input("Enter a number: "))
sum = 0
j = 1
while j <= n1:
    sum += j
    j += 1
print(f"The sum of the first {n} numbers is: ",sum)





