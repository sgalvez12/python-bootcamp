"""
    TODO: Create a function `line_generator` that has a parameter `number` and prints the following:
	Line 1
	Line 2
	...
	Line number
"""
def line_generator (number) :
    for item in range (number):
        print("Line", item + 1)

# TODO: Use the function once
line_generator(10)


