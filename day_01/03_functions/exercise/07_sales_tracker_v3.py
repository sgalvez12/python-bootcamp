def add(total):
    item_cost = int(input("Enter item cost: "))
    item_count = int(input("Enter item count: "))
    total_item_cost = item_cost * item_count
    return total + total_item_cost


def sub(total):
    item_cost = int(input("Enter item cost: "))
    item_count = int(input("Enter item count: "))
    total_item_cost = item_cost * item_count
    return total - total_item_cost




def show(total):
    print("Total: ", total)


def main():
    total = 0
    running = True
    while running:
        command = input("Provide command: ")
        if command == "add":
            total = add(total)
        if command == "sub":
            total = sub(total)
        if command == "show":
            show(total)
        elif command == "exit":
            running = False


main()
