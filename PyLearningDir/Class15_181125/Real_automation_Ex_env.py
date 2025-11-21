from dotenv import load_dotenv
import os
class LoginPage:

    def __init__(self,u_email,u_password):
        self.email = u_email
        self.password = u_password

    def LoginConfirmation(self):
        load_dotenv()
        if self.email == os.getenv("USERNAME1") and self.password == os.getenv("PASSWORD"):
            print("Login Successful!")
        else:
            print("Invalid Email or Password!")

email=input("Enter your email: ").strip()
password=input("Enter your password: ").strip()

login1 = LoginPage(email,password)
login1.LoginConfirmation()



