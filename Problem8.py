customers = {
    "Alice": 800,
    "Bob": 2500,
    "Carol": 6200,
    "David": 4700,
    "Emma": 9000
}

bronze = 0
silver = 0
gold = 0

for customer in customers:
    purchase_amount = customers[customer]

    if purchase_amount < 1000:
        tier = "Bronze"
        bronze = bronze + 1
    elif purchase_amount < 5000:
        tier = "Silver"
        silver = silver + 1
    else:
        tier = "Gold"
        gold = gold + 1

    print(customer, "-", tier)

print("Bronze Customers:", bronze)
print("Silver Customers:", silver)
print("Gold Customers:", gold)