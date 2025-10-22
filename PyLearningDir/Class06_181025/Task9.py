#reverse a number

n= int(input("Enter a number: ").strip())
reverse = 0

while n > 0:
    digit = n % 10          # Get the last digit
    reverse = reverse * 10 + digit  # Add it to the reversed number
    n = n // 10           # Remove the last digit
print("Reversed number:", reverse)

