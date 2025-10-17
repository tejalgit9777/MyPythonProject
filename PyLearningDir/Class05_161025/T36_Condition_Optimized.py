# check age is 21 and he/she can go to club.
#step 1 i/p age - int
#o/p is in string (result  - he/she can go to club

#step 2 Rough logic

"""
If age> 21 - can go to club
If age < 21 - Can't go to club
"""

age = int(input("Enter age: ").strip())

if age <= 0 or age > 130:
    print("Input valid age.")
else:
    if age >= 21:
        print("Can go to club")
    else:
        print("Can't go to club")