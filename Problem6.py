def calculate_months(loan_amount, interest_rate, monthly_payment):
    balance = loan_amount
    months = 0

    monthly_rate = (interest_rate / 100) / 12

    while balance > 0:
        interest = balance * monthly_rate
        balance = balance + interest
        balance = balance - monthly_payment
        months = months + 1

    return months


loan_amount = float(input("What is the loan amount? "))
interest_rate = float(input("What is the annual interest rate? "))
monthly_payment = float(input("What is the monthly payment? "))

first_month_interest = loan_amount * ((interest_rate / 100) / 12)

if monthly_payment <= first_month_interest:
    print("Monthly payment is too low to repay the loan.")
else:
    months = calculate_months(loan_amount, interest_rate, monthly_payment)

    print("Months to pay off loan:", months)
    