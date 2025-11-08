

# The user could provide an invalid integer input (string)
# TODO: Handle this case


# The user could give a negative number
# TODO: Handle this case

try:
    number = input("enter number: ")
    number_converted = int(number)
    if number_converted < 0:
        raise TypeError()
except ValueError:
    print("Enter a number value")
except  TypeError :
    print("Enter positive value")

# Challenge: TODO: Give the user infinite times to retry
