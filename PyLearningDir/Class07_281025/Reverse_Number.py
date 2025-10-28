#reverse a number

# n= int(input("Enter a number: ").strip())
# reverse = 0
#
# while n > 0:
#     digit = n % 10          # Get the last digit
#     reverse = reverse * 10 + digit  # Add it to the reversed number
#     n = n // 10           # Remove the last digit
# print("Reversed number:", reverse)

#Using For Loop

# for i in range(10,0,-1):
#     print(i,end=' ')


n=int(input("Enter Number: ").strip())
if 0< n <=100:
    for i in range(n, 0, -1):
        print(i, end=' ')
else:
    print("Invalid Number")




