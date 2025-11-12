# Filter

s2=[10,13,15,16,9,81,4]

def even_numbers(x):
    return x % 2 == 0

print(list(filter(even_numbers, s2)))

# def odd_numbers(x):
#     return x % 2 == 1

r1=list(filter(lambda x: x%2==1, s2))
print("Odd Numbers: ",r1)

s1=["","","Tejal","Shine"]
r2=list(filter(None,s1))
print("Remove Blank: ",r2)

s3=["PASS","FAIL","PASS","FAIL"]
r3=list(filter(lambda x: x=="PASS",s3))
r4=list(filter(lambda x: x!="PASS",s3))
print("Value which is pass: ",r3)
print("Value which is not pass: ",r4)

s4=set(x**2 for x in range(5))
print("Square of numbers: ",s4)