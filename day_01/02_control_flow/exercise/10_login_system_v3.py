# Expected password (you can change the value)
correct_password = "Shirley"

# Enter user password
password_input = input("Please provide password: ")

# TODO: Notify user if password is valid or invalid
correct_password_given = correct_password == password_input

if correct_password_given is True:
    print("Access Granted")
else:
    print("Access Denied")
