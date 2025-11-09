string = input('Enter string: ')
special_count = 0
special_char = '!@#$%^&*()'

# TODO: Add one to special_count for each special char in string
for schar in string:
    if schar in special_char:
        special_count += 1
print(special_count)
