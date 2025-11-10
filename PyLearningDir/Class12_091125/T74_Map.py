# Map
s1={33,44,11,66,77}

def square(x):
    return  x*x

print(square(33))
r=list(map(square,s1))
print(r)

print("====================")

name={"Tejal","Shine","Star",""}
name1=["BLUEBERRY","CRANBERRY","ICE APPLE","GRAPES"]

def upper_case(string):
    return string.upper()

r1=list(map(upper_case,name))
print("Upper case: ",r1)

def lower_case(string1):
    return string1.lower()

r2=list(map(lower_case,name1))
print("Lower case: ",r2)

print("====================")

m_sec={1200,4300,3200,7100}

def seconds(x):
    return x*1000

r3=list(map(seconds,m_sec))
print("Mile Seconds: ",r3)