prices = []

price = float(input("Enter an item price, or enter 0 to finish: "))

while price != 0:
    prices.append(price)
    price = float(input("Enter an item price, or enter 0 to finish: "))

total = sum(prices)
number_of_items = len(prices)

if number_of_items > 0:
    average = total / number_of_items
else:
    average = 0

print("Total purchase amount: $" , round(total, 2))
print("Average item cost: $" , round(average, 2))
print("Number of items bought:" , number_of_items)