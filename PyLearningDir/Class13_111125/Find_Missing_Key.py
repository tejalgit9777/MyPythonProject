#Find Missing Key

disc1={"a":1,"b":2,"c":3,"d":4}
disc2={"a":1,"c":4,"d":5}

m=set(disc1.keys())-set(disc2.keys())
m1=set(disc1.keys()-disc2.keys())
print(m)
print(m1)