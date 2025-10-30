from hashlib import sha1
from getpass import getpass
import sys


def register_user(username, password):
    password = sha1(password.encode("utf-8")).hexdigest()
    with open("users.txt", "a") as user_file:
        user_file.write(f"{username},{password}\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
        password = sys.argv[2]
        confirm_pass = sys.argv[3]
    else:
        username = input("Username: ")
        password = getpass("Password: ")
        confirm_pass = getpass("Confirm Password: ")

    if password == confirm_pass:
        register_user(username, password)
    else:
        print("Passwords do not match.")