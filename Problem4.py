sales = {
    "Alice": 5000,
    "Bob": 7000,
    "Carol": 3000,
    "Joe": 8000,
}

def calculate_commission(sale):
    commission = sale * 0.10
    return commission


ranked_employees = sorted(sales, key=sales.get, reverse=True)

rank = 1

for employee in ranked_employees:
    commission = calculate_commission(sales[employee])

    print(rank, ".", employee, "- Commission: $", commission)

    rank = rank + 1