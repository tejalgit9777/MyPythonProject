# Find minimum and maximum dictionary

disc1={"a":11,"b":2,"c":3,"d":4,"e":5,"f":66,"g":7}

def find_min():
    return min(disc1.values())

def find_max():
    return max(disc1.values())

print("Min Value: ",find_min())
print("Max Value: ",find_max())

print("=============================================")

def min_max_keys(k):
    return min(k.keys()), max(k.keys())

print("Min and max keys: ", min_max_keys({"a1":34,"a2":1,"a3":77,"a4":4}))

