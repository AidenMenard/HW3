expenses = {
    "Travel": [500, 200],
    "Meals": [40, 60, 30,70,50],
    "Supplies": [100]
}

grand_total = 0

# Loop through each category
for category in expenses:
    category_total = 0

    # Loop through each expense in the category
    for amount in expenses[category]:
        category_total = category_total + amount

    print(category, "Total: $", category_total)

    grand_total = grand_total + category_total

print("Grand Total: $", grand_total)