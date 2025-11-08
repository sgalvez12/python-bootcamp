# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"
admin_username = "admin"
admin_password = "admin"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

correct_credentials = username_input == correct_username and password_input == correct_password
admin_credentials = username_input == admin_username and password_input == admin_password

correct_credentials2 = (username_input == correct_username and password_input == correct_password) or (username_input == admin_username and password_input == admin_password)


# TODO: Notify user if credentials are valid or invalid
if correct_credentials or admin_credentials :
    print("Access Granted")
else:
    print("Access Denied")



if correct_credentials :
    print("Access Granted")
elif admin_credentials :
    print("Access Granted")
else:
    print("Access Denied")



if correct_credentials2 :
    print("Access Granted")
else:
    print("Access Denied")