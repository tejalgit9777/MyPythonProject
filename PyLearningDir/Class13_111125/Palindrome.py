# Palindrome

str1=str(input("Enter a string: ").strip())
revstr = ""
for char in reversed(str1):
    revstr = revstr + char
print("Reverse String: ",revstr)
if revstr == str1:
    print("Yes, the string is palindrome")
else:
    print("No, the string is not palindrome")

