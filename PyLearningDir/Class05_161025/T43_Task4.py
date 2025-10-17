# Check if the user can log in based on correct username and password.

username = str(input("Enter Username: ").strip())
password = int(input("Enter Password: ").strip())

if username == "admin" and password == 12345:
    print("✅ Logged In Successfully!")
else:
    print("Invalid Credentials!")