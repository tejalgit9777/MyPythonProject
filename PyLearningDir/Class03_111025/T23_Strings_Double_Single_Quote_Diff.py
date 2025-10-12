# Remove escape sequence use r

t = 'a'
t1 = 'a'
print(t)
print(t1)

print(type(t))
print(type(t1))

#t2 = 'C:\dir1\n.txt'
t2 = r"C:\dir1\n.txt" #raw it will print as it is( ignoring escape sequence)
print(t2)

p = r"https://chat.openai.com/c/b890b1e3-5c56-41cf-bedb-983508f9a824"
print(p)



