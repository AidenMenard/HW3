portfolio = {
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130}
}

total_value = 0

for stock in portfolio:
    shares = portfolio[stock]["shares"]
    price = portfolio[stock]["price"]

    stock_value = shares * price

    print(stock, "Value: $", stock_value)

    total_value = total_value + stock_value

print("Total Portfolio Value: $", total_value)