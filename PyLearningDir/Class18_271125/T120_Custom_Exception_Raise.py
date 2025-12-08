
class  InvalidAgeError(Exception):
    pass

def user_reg_age(age):
    if age < 18:
        raise InvalidAgeError("Invalid age!")
    else:
        print("User registered successfully!")

try:
    user_reg_age(-1)
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)

