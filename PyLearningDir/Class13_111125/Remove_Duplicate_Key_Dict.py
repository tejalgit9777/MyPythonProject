# Remove duplicate key from dictionary

disc1={"a":11,"b":3,"b":5,"d":4,"e":7,"f":66,"g":7}
s=set()
d={}

for key, value in  disc1.items():
    if key not in d:
        d[key]=value
        s.add(key)
print(s)
print(d)