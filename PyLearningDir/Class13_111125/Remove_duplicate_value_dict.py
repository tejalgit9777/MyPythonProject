# Remove duplicate value from dictionary

disc1={"a":11,"b":3,"c":3,"d":4,"e":7,"f":66,"g":7}
s=set()
d={}
for key, value in disc1.items():
    if value not in s:
        d[key]= value
        s.add(value)
print(d)
print(s)


