# Set functions - Union, Intersection, Difference, Symmetric Difference

# Union or you can use symbol '|' ==> It will give all value including common value but not repeating value.
print("Union")
n={1,2,3,4,5,6}
n1={4,7,8,9}

print(n.union(n1))
print(n | n1)

#Intersection or you can use '&' symbol ==> It will give common value from both sets.
print("Intersection")
print(n.intersection(n1))
print(n & n1)

# Difference or you can use ("-")symbol ==> It will give unique value which is not in other set.
print("Difference")
print(n.difference(n1))
print(n-n1)
print("\n")
print(n1-n)

# Symmetric Difference or you can use "^" symbol
# It will give values except value presents in both sets.
s={33,44,11,66,77}
s1={33,44,22,78,99}

print("Symmetric difference")
print(s.symmetric_difference(s1))
print(s ^ s1)
print("\n")
print(s1 ^ s)