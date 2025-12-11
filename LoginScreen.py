import getpass
from Main_Menu import main 

# Default Username and Password
users = {"admin": "1234","Jovan":"jovan"}

print("=== LOGIN SYSTEM ===")

while True:
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if username in users and users[username] == password:
        print("\nLogin successful!")
        main()
        
        break
    else:
        print("Invalid username or password. Try again.\n")
