test_dict={
            "name": "Tejal",
            "age": 36,
            "Address":
                {
                    "Home Address":"Surat",
                    "Office Address":"Navsari"
                },
            "Height" : 5.3,
            "Female" : True
}
test_dict3={
            "name1": "Teju",
            "age1": 36,
            "Address1": "Radhaswami Society",
            "Height1" : 5.3,
            "Female1" : True
}

test_dict1=dict(name="Shine",age= 25,Address="Adajan",Height=5.4,Female=True)


print(test_dict)
print(test_dict1)
all_list=[test_dict,test_dict1]
print(all_list)
print(all_list[0])
print(all_list[1])
print(all_list[0]["Address"]["Home Address"])
print(all_list[0]["Address"]["Office Address"])

 # Zip function

key= ["Name","Age","Address"]
Value=["Tejal",36,"Surat"]
list3= dict(zip(key,Value))
print(list3)

# # Merge
print("====================Merge===============")
all_list1 = test_dict | test_dict3
print(all_list1)
print(all_list1.get("name"))
print(all_list1.get("name1"))