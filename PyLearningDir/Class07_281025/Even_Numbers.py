# print even numbers
from queue import PriorityQueue

# for loop
n = int(input("Enter Number: ").strip())
for i in range(1, n):
    if i % 2 == 0:
        print(i)


# while loop
j = 1
while j <= 20:
    if j % 2 == 0:
        print(j)
    j += 1


