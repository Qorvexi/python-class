email = "admin@yahoo.com"
password = "admin123"

email1 = input("Enter email")
password1 = input("Enter password")

if email1 == email:
    print("Access Granted, Welcome to the Student Managing System (SMS)")
else:
    print("Access Denied, Invalid Email and Password")

if password1 == password:
    print("Access Granted, Welcome to the Student Managing System (SMS)")
else:
    print("Access Denied, Invalid Email and Password")