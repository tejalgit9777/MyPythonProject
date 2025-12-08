def login(user):
     if user != "admin":
        #print("Invalid User")
        raise Exception("Unauthorized Access!")
     else:
         print("Login Successful")
login("admin1")
#login("admin")