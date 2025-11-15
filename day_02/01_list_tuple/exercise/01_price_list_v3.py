prices = [10_000, 20, 3_000, 3, -200, 1_000]

# TODO: Print the first, third, and last item
print("Current Price:", prices[0])
print("Current Price:", prices[2])
print("Current Price:", prices[-1])

# TODO: Change the first, third, and last values to half the price
prices [0] //= 2
prices [2] //= 2
prices [-1] //=2
# TODO: Print the first, third, and last item again to see new price
print("New Price:", prices[0])
print("New Price:", prices[2])
print("New Price:", prices[-1])

# TODO: Remove the negative price in the list
for price in prices:
    if price < 0:
        prices.remove(price)
        print(prices)