# Dictionary

test_dict={
            "name": "Tejal",
            "age": 36,
            "Address": "Radhaswami Society",
            "Height" : 5.3,
            "Female" : True
}

print(test_dict)

print(test_dict["name"])
print(test_dict["age"])
print(test_dict["Address"])
print(test_dict["Height"])
print(test_dict["Female"])
print(test_dict["age"])
print("===================================")
for key,value in test_dict.items():
    print(key,":",value)
    print(key,"\n")
    print(value)

# Update key value
test_dict["name"]="Teju"
print(test_dict)

