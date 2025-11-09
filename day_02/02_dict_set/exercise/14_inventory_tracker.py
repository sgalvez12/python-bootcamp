from operator import itemgetter


def add(inventory):
    name = input("Enter Item: ")
    info = input("Enter Info: ")
    stock = int(input("Enter Stock: "))

    item = {"name": name, "info": info, "stock": stock}
    """TODO:
        Ask for item name, info, and stock
        Create a dictionary with key: name, info, stock
        Add that dictionary to inventory
    """

    inventory.append(item)

def remove(inventory):
    """TODO:
        Ask for item index (int)
        Remove item in that index in inventory
    """


def read(inventory):
    """TODO:
        Ask for item index (int)
                Show item in that index in inventory
    """
def show(inventory):
    """TODO: Print items line-by-line"""

def main():
    """Created to test functions"""
    running = True
    item_detail = str | int | float
    inventory: list[dict[str, item_detail]] = []

    while running:
        command = input("Command: ")
        if command == "add":
            add(inventory)
            pass
        elif command == "remove":
           remove(inventory)
            pass
        elif command == "read":
            print(inventory)
            pass
        elif command == "show":
            # TODO: Use show command"""
            pass
        elif command == "exit":
            running = False


main()
