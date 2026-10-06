warehouses = [
    {
        "name": "Warehouse A",
        "inventory": {
            "apples": 100,
            "bananas": 150
        }
    },
    {
        "name": "Warehouse B",
        "inventory": {
            "apples": 200,
            "bananas": 100
        }
    }
]

total_inventory = {}

for warehouse in warehouses:
    for product in warehouse["inventory"]:
        amount = warehouse["inventory"][product]

        if product in total_inventory:
            total_inventory[product] = total_inventory[product] + amount
        else:
            total_inventory[product] = amount

for product in total_inventory:
    print(product, "Total Stock:", total_inventory[product])