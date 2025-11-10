# Print First not repeating character

#string1="SWISS"

s=set()

def first_unique_char(string2):
    for char in string2:
        if string2.count(char)==1:
            s.add(char)
            return char
    return None

r1=first_unique_char("SWISS")
print(first_unique_char("SHINESTAR"))
print(r1)
print(s)