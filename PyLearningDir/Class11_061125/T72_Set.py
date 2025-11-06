# Set is Immutable but not allow duplicate items
"""
    Test Test
"""

list1 = {1,5,6,7,3,1,66,77,1111}
print(list1)

for item in list1:
    print(item, end=' || ')

print("\n")
list1.add(33)
print(list1)

print("\n")
list1.remove(66)
print(list1)

print("\n")
list1.pop()
print(list1)



