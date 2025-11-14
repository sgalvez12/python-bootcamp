# TODO: Ask the user how many items will be calculated
input_count = int(input("How many will be calculated? "))
total = 0

# TODO: Use a for loop to ask for more than one cost and count
for item in range(1, input_count + 1):
    item_cost = int(input(f"Item {item} cost: "))  # Let the user enter a number
    item_count = int(input(f"Item {item} count: "))  # Let the user enter a number
    item_total = item_cost * item_count
    total += item_total


print(total)
