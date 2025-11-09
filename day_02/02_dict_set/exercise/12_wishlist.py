# TODO: Fill in the details of the item you plan to buy
order = {
    "Name": "Shirley",
    "Info": "Yeye",
    "Height": 162,
    "Title": "Mom"
}

# TODO: Print the item details in the following format:
"""
Order:
	Name: item name
	Info: item info
	...
"""
for key, value in order.items():
    print(f"\t{key}:  {value}")