username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "password":
    print("Login Successful!")
elif not username or not password:
    print("Missing Credentials!")
else:
    print("Login Failed!")
