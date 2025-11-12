# Question - ✅ Count vowels and consonants in a String

str1="shinest@r !!"

vowels="aeiouAEIOU"
v=0
consonants=0
res=list()
res1=list()
for char in str1:
    if char.isalpha() == True:
            if char in vowels:
                v += 1
                res.append(char)
            else:
                consonants += 1
                res1.append(char)

print(res)
print("Vowels:" ,v)
print(res1)
print("Consonants: ",consonants)