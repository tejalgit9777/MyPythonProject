# Tuple - Immutable

list1 = (1,5,6,3,1)
print(list1)

for item in list1:
    print(item, end=' || ')

print("\n")

print("convert in list")
list2 = list(list1)
print(list2)

print("convert in tuple")
list3 = tuple(list1)
print(list3)

print("convert in Set")
list4 = set(list1)
print(list4)

