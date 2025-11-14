prices = [10_000, 20, 3_000, 3, -200, 1_000]

for item in prices:
    if item < 0:
        prices.remove(item)
        print(prices)

# TODO: Print the first, third, and last item
print("Current Price:", prices[0])
print("Current Price:", prices[2])
print("Current Price:", prices[-1])
