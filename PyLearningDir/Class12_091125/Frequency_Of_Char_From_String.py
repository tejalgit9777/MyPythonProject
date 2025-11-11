# Find frequency of character from string

string1="shinestar"
freq= {}

for char in string1:
    freq[char]=freq.get(char,0)+1
print(freq,end=" ")
#====================================================
print("with user input")
str1=str(input("Enter a string: ").strip())
freq1={}
for char1 in str1:
    freq1[char1]=freq1.get(char1,0)+1
print(freq1)