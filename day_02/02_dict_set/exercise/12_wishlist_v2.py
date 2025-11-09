# TODO: Fill in the details of the items you plan to buy
parents = [
    {"Name": "Shirley",
    "Info": "Yeye",
    "Height": 162,
    "CS": "Single"
    },
    {"Name": "Phen",
    "Info": "Penda",
    "Height": 153,
    "CS": "Married"
    },
    {"Name": "Carla",
    "Info": "Chay",
    "Height": 120,
    "CS": "Single"
    }
]

print(parents)
for parent in parents:
    print("Parent:")
    for key, value in parent.items():
        print(f"\t{key}: {value}")

# TODO: Print the item details in the following format (for each order):
"""
Order:
	Name: item name
	Info: item info
	...
"""
