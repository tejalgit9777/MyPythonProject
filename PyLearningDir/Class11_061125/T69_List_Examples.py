# List - mutable


#fav_fruits = ["apple", "banana", "cherry","Blueberry"]

my_list=[11,43,43,67,89,True,False,4.5,"shine",'A',"shine"]
print(my_list)

print("\n")
#In For loop
for item in my_list:
    print(item, end=" || ")

# functions
print("\n")

for item in my_list:
    print(item, end=" || ")

print("\n")
print("Appending items:")
my_list.append(7777)
print(my_list)

print("\n")
print("Insert items:")
my_list.insert(2,'T')
print(my_list)

print("\n")
print("Remove items:")
my_list.remove(False)
print(my_list)

print("\n")
print("Extended items:")
my_list.extend([11,22,"Shinestar"])
print(my_list)

print("\n")
print("Remove last items:")
my_list.pop()
print(my_list)

print("\n")
print("Reverse items:")
my_list.reverse()
print(my_list)
my_list.reverse(),-1
print(my_list)

print("\n")
print("Replace items:")
my_list[1]="Crenberry"
print(my_list)
my_list[-1]="Hello"
print(my_list)

print("\n")
print("Count items:")
print(len(my_list))

print("\n")
print("Count items")
print(my_list.count(43))

print("\n")
print("Index value items")
print(my_list.index('T'))
print("\n")

my_list2=[335,22,54,0,8,11]
print(my_list2)
print("\n")
print("Sort and reverse sorted item:")
my_list2.sort()
print(my_list2)
my_list2.sort(reverse=True)
print(my_list2)
print("Copy list")
my_list2.copy()
print(my_list2)
