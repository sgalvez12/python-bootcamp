"""
    TODO: Create a function `line_generator` that has a parameter `number` and prints the following:
	Line 1
	Line 2
	...
	Line number
"""
def line_generator (number) :
    for item in range (1, number + 1):
        print(f"Line {item}")

# TODO: Use the function once
line_generator(10)


